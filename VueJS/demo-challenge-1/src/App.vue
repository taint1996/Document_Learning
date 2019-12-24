<template>
  <div id="app">
    <b-container fluid class="bv-example-row">
        <b-col cols="12">
          <b-form inline>
            <b-form-input class="inp-search" placeholder="Tìm kiếm"/>
            <b-button-group>
              <b-button variant="secondary" class="btn-search">Search</b-button>
              <b-button variant="secondary">Thêm mới</b-button>
              <b-button variant="secondary">Đóng lại</b-button>
            </b-button-group>
          </b-form>
        </b-col>

        <b-row>
          <b-col cols="8">
            <div class="mt-5">
              <b-table hover :fields="fields" :items="items">
                <template v-slot:cell(order_no)="data">
                  {{ data.index + 1 }}
                </template>

                <template v-slot:cell(adminstrator)="data">
                  <span v-html="data.value"></span>
                </template>
              </b-table>
            </div>
          </b-col>

          <b-col cols="4">
            <div class="add-new-form">
              <h2 class="text-center">Thêm Mới</h2>
              <b-form @submit="onSubmit" v-if="show">
                <b-form-group
                  id="input-group-1"
                  label="Tên:"
                  label-for="input-1"
                >
                  <b-form-input
                    id="input-group-2"
                    v-model="form.email"
                    required
                    label-for="input-2"
                    placeholder="Nhập tên của bạn"
                  ></b-form-input>
                </b-form-group>

                <b-form-group
                  id="input-group-3"
                  label="Số tiền:"
                  label-for="input-3"
                >
                  <b-form-input id="input-group-4"
                    label-for="input-4"
                    v-model="form.email"
                    required
                    placeholder="Nhập số tiền"
                  ></b-form-input>
                </b-form-group>

                <b-form-group label="Ngày:" label-for="inp-date">
                  <datepicker id="inp-date"
                              :format="format"
                  ></datepicker>
                </b-form-group>

                <b-form-group label="Hình thức thanh toán:" label-for="input-6">
                  <b-form-select
                    id="input-group-6"
                    v-model="form.payment_type"
                    :options="payment_types"
                    required
                  ></b-form-select>
                </b-form-group>

                <b-form-group label="Chi phí:" label-for="input-7">
                  <b-form-select
                    id="input-group-7"
                    v-model="form.cost"
                    :options="costs"
                    required
                  ></b-form-select>
                </b-form-group>

                <b-form-group label="Nội dung" label-for="input-8">
                  <b-form-textarea
                    id="input-group-8"
                    placeholder="Nhập nội dung"
                    required
                    size="lg"
                  ></b-form-textarea>
                </b-form-group>

                <b-form-group>
                  <b-button type="button" variant="primary">Lưu</b-button>
                </b-form-group>
              </b-form>
            </div>
          </b-col>
        </b-row>
    </b-container>
  </div>
</template>

<script>
import Datepicker from 'vuejs-datepicker';

export default {
  name: 'app',
  components: {
    Datepicker
  },
  data() {
    return {
      format: "dd/MM/yyyy",
      fields: [
        { key: 'order_no', label: 'STT'},
        { key: "name", label: "Tên" },
        { key: "date_of_birth", label: "Ngày sinh"},
        { key: "money", label: "Số Tiền"},
        { key: "payment_type", label: "Hình thức thanh toán" },
        { key: "cost", label: "Chi phí"},
        { key: "content", label: "Nội dung"},
        { key: "adminstrator", label: "Quyền" }
      ],
      items: [
        { date_of_birth: "12/11/2019", name: "Nguyên Ngọc Sơn", money: "2500000", payment_type: 'CK', cost: "CSKH", content: "Nội dung", adminstrator: '<button variant="danger">Btn 1</button><button variant="info">Btn 2</button>'},
        { date_of_birth: "12/11/2019", name: "Nguyên Ngọc Sơn", money: "2500000", payment_type: 'CK', cost: "CSKH", content: "Nội dung", adminstrator: '<button variant="danger">Btn 1</button><button variant="info">Btn 2</button>'},
        { date_of_birth: "12/11/2019", name: "Trần Bảo Ngọc", money: "1350000", payment_type: 'CK', cost: "CSKH", content: "Nội dung", adminstrator: '<button variant="danger">Btn 1</button><button variant="info">Btn 2</button>'},
        { date_of_birth: "12/11/2019", name: "Huỳnh Thuý Vy", money: "500000", payment_type: 'TM', cost: "NVL", content: "Nội dung", adminstrator: '<button variant="danger">Btn 1</button><button variant="info">Btn 2</button>' }
      ],

      form: {
        name: '',
        money: '',
        payment_type: null,
        cost: null,
        content: ''
      },
      payment_types: [{ text: 'Chọn hình thức thanh toán', value: null }, 'Thanh toán tiền mặt', 'Chuyển khoản'],
      costs: [{ text: 'Chọn chi phí', value: null }, 'CSKH', 'NVL'],
      show: true
    }
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault()
      alert(JSON.stringify(this.form))
    }
  }
}
</script>

<style scoped lang="scss">
  #app {
    font-family: Arial, Helvetica, sans-serif;
    color: #2c3e50;
    margin-top:3em;

    .inp-search {
      border-top-right-radius: 0px;
      border-bottom-right-radius: 0px;
    }
    .btn-search {
      border-radius: 0;
    }

    .add-new-form {
      border: 2px solid lightgray;
      padding: 3em;
    }
  }
</style>

<style>
  input#inp-date {
    width: 100%;
    border: 1px solid lightgray;
    padding: 0.375rem 0.75rem;
    border-radius: 0.25em;
  }
</style>
