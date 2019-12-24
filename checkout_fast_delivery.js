var checkoutFastDelivery = (function() {

  const DEFAULT_APPLY_FAST_DELIVERY_VALUE = "false";
  const DEFAULT_PAYMENT_TYPE_VALUE = "cart_payment_type_cod";

  const TOTAL_ORDER_VALUE = 5000000;

  function getFastDeliveryFee(callback) {
    $.ajax({
      method: 'GET',
      url: Routes.get_fast_delivery_fee_path($('#cart_id').val()),
      dataType: 'json'
    }).done((result) => {
      callback(result)
    })
    .fail((error) => {
      console.log("ERROR: ", error);
    })
  }

  /////// Alert and update checked fast delivery message
  function swalWithBootstrapButton() {
    return Swal.mixin({
      customClass: {
        confirmButton: 'btn btn-success mr-3',
        cancelButton: 'btn btn-danger'
      },
      buttonsStyling: false
    })
  }

  function showSwalErrorMessage() {
    swalWithBootstrapButton().fire({
      type: 'warning',
      title: I18n.t('checkout.fast_delivery.error_title'),
      html: `<p>${I18n.t('checkout.fast_delivery.apply_within_total')} <b>${Utils.to_currency(TOTAL_ORDER_VALUE)}</b></p> <div>${I18n.t('checkout.fast_delivery.want_to_continue')}</div>`,
      confirmButtonText: I18n.t('checkout.fast_delivery.continue'),
      cancelButtonText: I18n.t('checkout.fast_delivery.back_to_cart'),
      showConfirmButton: true,
      showCancelButton: true
    }).then((result) => {
      if (result.value) {
        $('.custom-chkbox-fast-delivery').remove();
        useFastDeliveryFee.removeAppliedCustomFastDelivery();
      } else if (result.dismiss === Swal.DismissReason.cancel){
        window.location.href = Routes.cart_path();
      }
    })
  }

  function totalAppliedFastDelivery(fee) {
    var totalCOD = parseInt($('#checkout-total-cod').data('total'));
    var totalTransfer = parseInt($('#checkout-total-transfer').data('total'));

    $('.checkout-total-number').text(Utils.to_currency(totalCOD + fee));
    $('.checkout-total-discount').text(Utils.to_currency(totalTransfer + fee));
    $('.transport-fee').text(Utils.to_currency(fee));
  }

  function errorFastDeliveryCheckoutTotal(checkoutTotal) {
    if (checkoutTotal >= TOTAL_ORDER_VALUE) {
      checkoutFastDelivery.showSwalErrorMessage();
    }
  }

  function onLoadErrorFastDeliveryTotal(checkoutTotal) {
    feeDeliveries.db.rememberDataFastDelivery($('#cart_id').val(), (fastDelivery) => {
      if (fastDelivery.applied_fast_delivery === "true" && checkoutTotal >= TOTAL_ORDER_VALUE) {
        errorFastDeliveryCheckoutTotal(checkoutTotal);
      }
    })
  }

  function cartSetDefaultNewOrder() {
    if (window.location.pathname === "/cart") {
      var orderId = $('.checkout-button').attr('data-cart-id');

      feeDeliveries.db.save(orderId, DEFAULT_PAYMENT_TYPE_VALUE, DEFAULT_APPLY_FAST_DELIVERY_VALUE);
    }
  }

  function initDiscount(paymentType) {
    if (paymentType == 'cod') {
      $('.total-no-discount').show();
      $('.total-with-discount').hide();
      $('.product-with-discount').addClass('d-none').removeClass('d-flex');
    }
    else if (paymentType == 'bank_transfer') {
      $('.total-no-discount').hide();
      $('.total-with-discount').show();
      $('.product-with-discount').removeClass('d-none').addClass('d-flex');
    }
  }

  return {
    getFastDeliveryFee: getFastDeliveryFee,

    showSwalErrorMessage: showSwalErrorMessage,
    onLoadErrorFastDeliveryTotal: onLoadErrorFastDeliveryTotal,
    errorFastDeliveryCheckoutTotal: errorFastDeliveryCheckoutTotal,

    totalAppliedFastDelivery: totalAppliedFastDelivery,

    cartSetDefaultNewOrder: cartSetDefaultNewOrder,
    initDiscount: initDiscount
  }
})(jQuery)