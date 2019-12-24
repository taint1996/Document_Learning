var useFastDeliveryFee = (function() {

  const DEFAULT_DELIVERY_FEE = 0;
  const TOTAL_ORDER_VALUE = 5000000;

  function rememberApplyFastDelivery() {
    if(feeDeliveries.db) {
      feeDeliveries.db.rememberDataFastDelivery($('#cart_id').val(), (fastDelivery) => {
        var $paymentType = $(`#${fastDelivery.payment_type}`);

        $paymentType.attr('checked', true);
        $('.chk-apply-fast-delivery').attr('checked', fastDelivery.applied_fast_delivery === "true" ? true : false);

        checkoutFastDelivery.initDiscount($paymentType.val());

        if ($('.chk-apply-fast-delivery:checked').length > 0) {
          addAppliedCustomFastDelivery();
        } else {
          removeAppliedCustomFastDelivery();
        }
      })
    }
  }

  function onChangeFastDelivery() {
    $('.chk-apply-fast-delivery').on('change', function(e) {
      if (e.target.checked) {
        $.ajax({
          method: 'GET',
          url: Routes.get_fast_delivery_fee_path($('#cart_id').val())
        }).done((result) => {
          addAppliedCustomFastDelivery();
        }).fail((error) => {
          console.log("ERROR: ", error);
        })
      } else {
        removeAppliedCustomFastDelivery();
      }
      checkoutFastDelivery.errorFastDeliveryCheckoutTotal(parseInt($($('.checkout-total').children("span")).attr('data-total')));
      updateDataFastDelivery();
    })
  }

  function addAppliedCustomFastDelivery() {
    $('.transport-fee').addClass('fast-delivery-fee');
    $('.real-transport-fee').addClass('d-none');

    $('.chk-apply-fast-delivery').attr('value', "true");
    $('.chk-apply-fast-delivery').prop('checked', true);

    checkoutFastDelivery.getFastDeliveryFee((fee) => {
      checkoutFastDelivery.totalAppliedFastDelivery(fee.order_fee);
    })
  }

  function removeAppliedCustomFastDelivery() {
    $('.transport-fee').removeClass('fast-delivery-fee');
    $('.real-transport-fee').removeClass('d-none');

    $('.chk-apply-fast-delivery').attr('value', "false");
    $('.chk-apply-fast-delivery').prop('checked', false);

    checkoutFastDelivery.totalAppliedFastDelivery(DEFAULT_DELIVERY_FEE);
  }

  function updateDataFastDelivery() {
    if (feeDeliveries.db) {
      var orderId = $("#cart_id").val();
      var paymentType = $('.js-payment-type-radio:checked').attr('id');
      var checkedAppliedFastDelivery = $('.chk-apply-fast-delivery').prop('checked');

      if (checkedAppliedFastDelivery !== undefined) {
        feeDeliveries.db.updateObjDataFastDelivery(orderId, paymentType, checkedAppliedFastDelivery === true ? "true" : "false");
      } else {
        feeDeliveries.db.updatePaymentTypeFastDelivery(orderId, paymentType);
      }
    }
  }

  function optionCheckboxFastDeliveryHTML(fee) {
    var inputCheckboxDeliveryHTML = `<input type='checkbox' name='is_check_delivery' value='false' id="is_check_delivery" class='custom-control-input chk-apply-fast-delivery'/>    <label class='custom-control-label' for='is_check_delivery'>${ I18n.t('checkout.fast_delivery.title') }</label>  <div class='text-muted transport-fee-notice'>${ I18n.t('checkout.fast_delivery.notice', { fee: Utils.to_currency(fee)}) }</div>`;

    var textInfoDeliveryHTML = `<div><p class='small mb-0'><i class='fa fa-info-circle text-info'></i><span class='pl-1'>${ I18n.t('checkout.fast_delivery.commit_to_delivery_within_24h') }</span></p>   <p class='small mb-0'><i class='fa fa-info-circle text-info'></i><span class='pl-1'>${ I18n.t('checkout.fast_delivery.apply_order_fast_delivery') }</span></p>    <p class='small mb-0'><i class='fa fa-info-circle text-info'></i><span class='pl-1'>${ I18n.t('checkout.fast_delivery.apply_fast_delivery_order_less_than_5M') }</span></p></div></div>`

    const fastDeliveryFee = `<div class='custom-control custom-checkbox mt-1 mb-1 custom-chkbox-fast-delivery'>` + inputCheckboxDeliveryHTML + textInfoDeliveryHTML + `</div>`;

    $(fastDeliveryFee).insertAfter($('.product-with-discount'));

    var inputCheckboxDeliveryTabletHTML = `<input type='checkbox' name='is_check_delivery' value='false' id="is_check_delivery" class='custom-control-input chk-apply-fast-delivery'/>    <label class='custom-control-label' for='is_check_delivery'>${ I18n.t('checkout.fast_delivery.title') }</label>  <div class='text-muted transport-fee-notice'>${ I18n.t('checkout.fast_delivery.notice', { fee: Utils.to_currency(fee)}) }</div>`;

    const fastDeliveryFeeTablet = `<div class='custom-control custom-checkbox mt-1 mb-1 custom-chkbox-fast-delivery'>` + inputCheckboxDeliveryTabletHTML + `</div>`;

    $(fastDeliveryFeeTablet).insertAfter($('.product-with-discount-tablet'));
  }

  function applyFastDeliveryForHCMCity(data) {
    if (data.is_hcm) {
      checkoutFastDelivery.getFastDeliveryFee((fastDeliveryFee) => {
        ////////// show alert message when applied fast delivery is true and total number greater than 5M
        const checkoutTotal = parseInt($($('.checkout-total').children("span")).attr('data-total'));
        checkoutFastDelivery.onLoadErrorFastDeliveryTotal(checkoutTotal);

        if (checkoutTotal < TOTAL_ORDER_VALUE) {
          optionCheckboxFastDeliveryHTML(fastDeliveryFee.order_fee);
        }

        onChangeFastDelivery();
        rememberApplyFastDelivery();
      })
    } else {
      removeAppliedCustomFastDelivery();
      $('.custom-chkbox-fast-delivery').remove();
    }
    rememberApplyFastDelivery();
  }

  function checkoutApplyFastDeliveryForHCMCity(data) {
    if (window.location.pathname === '/checkout') {
      applyFastDeliveryForHCMCity(data);
    }
  }

  function applyFastDeliveryCharge() {
    var cityId = $('.js-address-city option:selected').prop('value');

    if (cityId) {
      $.ajax({
        method: 'GET',
        url: Routes.api_addresses_sub_addresses_path(),
        data: {
          region_id: cityId
        }
      }).done((result) => {
        applyFastDeliveryForHCMCity(result.data);
      }).fail((result) => {
        console.error("ERROR: ", result);
      });
    }
    rememberApplyFastDelivery();
  }

  function checkoutApplyFastDeliveryCharge() {
    if (window.location.pathname === '/checkout') {
      applyFastDeliveryCharge();
    }
  }

  return {
    checkoutApplyFastDeliveryCharge: checkoutApplyFastDeliveryCharge,
    checkoutApplyFastDeliveryForHCMCity: checkoutApplyFastDeliveryForHCMCity,

    updateDataFastDelivery: updateDataFastDelivery,
    rememberApplyFastDelivery: rememberApplyFastDelivery,
    removeAppliedCustomFastDelivery: removeAppliedCustomFastDelivery
  }
})(jQuery);
