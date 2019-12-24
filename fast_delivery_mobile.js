var useFastDeliveryFee = (function() {

  const DEFAULT_DELIVERY_FEE = 0;

  const TOTAL_ORDER_VALUE = 5000000;

  function rememberApplyFastDelivery() {
    if(feeDeliveries.db) {
      feeDeliveries.db.rememberDataFastDelivery($('#cart_id').val(), (fastDelivery) => {
        var $paymentType = $(`#${fastDelivery.payment_type}`);

        $paymentType.attr('checked', true);
        $('.chk-apply-fast-delivery-mobile').attr('checked', fastDelivery.applied_fast_delivery === "true" ? true : false);

        checkoutFastDelivery.initDiscount($paymentType.val());

        if ($('.chk-apply-fast-delivery-mobile:checked').length > 0) {
          addAppliedCustomFastDelivery();
        } else {
          removeAppliedCustomFastDelivery();
        }
      })
    }
  }

  function onChangeFastDelivery() {
    $('.chk-apply-fast-delivery-mobile').on('change', function(e) {
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
      checkoutFastDelivery.errorFastDeliveryCheckoutTotal($($('.checkout-total-mobile').children("span")).attr('data-total'));
      updateDataFastDelivery();
    })
  }

  function addAppliedCustomFastDelivery() {
    $('.transport-fee').addClass('fast-delivery-fee');
    $('.real-transport-fee').addClass('d-none');

    $('.chk-apply-fast-delivery-mobile').attr('value', "true");

    checkoutFastDelivery.getFastDeliveryFee((fee) => {
      checkoutFastDelivery.totalAppliedFastDelivery(fee.order_fee);
    })
  }

  function removeAppliedCustomFastDelivery() {
    $('.transport-fee').removeClass('fast-delivery-fee');
    $('.real-transport-fee').removeClass('d-none');

    $('.chk-apply-fast-delivery-mobile').attr('value', "false");

    checkoutFastDelivery.totalAppliedFastDelivery(DEFAULT_DELIVERY_FEE);
  }

  function updateDataFastDelivery() {
    if (feeDeliveries.db) {
      var orderId = $("#cart_id").val();
      var paymentType = $('.js-payment-type-radio:checked').attr('id');
      var checkedAppliedFastDelivery = $('.chk-apply-fast-delivery-mobile').prop('checked');

      if (checkedAppliedFastDelivery !== undefined) {
        feeDeliveries.db.updateObjDataFastDelivery(orderId, paymentType, checkedAppliedFastDelivery === true ? "true" : "false");
      } else {
        feeDeliveries.db.updatePaymentTypeFastDelivery(orderId, paymentType);
      }
    }
  }

  function optionCheckboxFastDeliveryHTML(fee) {
    var inputCheckboxDeliveryMobileHTML = `<input type='checkbox' name='is_check_delivery' value='false' id="is_check_delivery_mobile" class='custom-control-input chk-apply-fast-delivery-mobile'/>    <label class='custom-control-label' for='is_check_delivery_mobile'>${ I18n.t('checkout.fast_delivery.title') }</label>  <div class='text-muted transport-fee-notice'>${ I18n.t('checkout.fast_delivery.notice', { fee: Utils.to_currency(fee)}) }</div>`;

    const fastDeliveryFeeMobile = `<div class='custom-control custom-checkbox mt-1 mb-1 custom-chkbox-fast-delivery'>` + inputCheckboxDeliveryMobileHTML + `</div>`;

    $(fastDeliveryFeeMobile).insertAfter($('.transport-fee-mobile'));
  }

  function applyFastDeliveryForHCMCity(data) {
    if (data.is_hcm) {
      checkoutFastDelivery.getFastDeliveryFee((fastDeliveryFee) => {
        const checkoutTotal = parseInt($($('.checkout-total-mobile').children("span")).attr('data-total'));
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
