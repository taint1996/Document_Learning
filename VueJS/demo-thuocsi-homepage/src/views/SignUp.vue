<template>
  <div class="sign-up-form">
    <header class="header-no-nav">
      <div class="justify-content-between d-flex">
        <b-link href="/" class="top-nav-thuocsi-logo">
          <img alt="thuocsi logo" src="../assets/images/thuocsi-logo.png" class="logo lozad img-fluid loaded" />
        </b-link>


        <b-link href="tel:02862848680"  class="top-nav-contact-us">
          <font-awesome-icon :icon="['fas', 'phone-square']" class="icon-phone-square" />
          <span class="contact-us-text">
            02 862 848 680
            <div class="text-dark small">(8:00 - 18:00, T2 - T7)</div>
          </span>
        </b-link>
      </div>
    </header>

    <b-container>
      <b-row align-h="center">
        <b-col cols="5">
          <div class="p-3 card-login-form">
            <h3 class="mb-4 login-title">Tạo tài khoản</h3>

            <b-form @submit="onSubmit" @reset="onReset" v-if="show">
              <b-form-group
                id="input-group-1"
                label="Họ tên:"
                label-for="input-1"
              >
                <b-form-input
                  id="input-1"
                  v-model="form.name"
                  type="text"
                  required
                  placeholder="Nhập họ tên"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-2"
                label="Số điện thoại:"
                label-for="input-2"
              >
                <b-form-input
                  id="input-2"
                  v-model="form.phone_number"
                  required
                  type="text"
                  placeholder="Nhập số điện thoại"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-2"
                label="Email:"
                label-for="input-2"
              >
                <b-form-input
                  id="input-2"
                  v-model="form.email"
                  required
                  type="text"
                  placeholder="Nhập email"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-1"
                label="Password:"
                label-for="input-1"
              >
                <b-form-input
                  id="input-1"
                  v-model="form.password"
                  type="text"
                  required
                  placeholder="Nhập mật khẩu"
                ></b-form-input>
              </b-form-group>
              <b-row class="justify-content-center">
                <b-col cols="12" class="text-center">
                  <p>
                    <span class="text-danger">
                      <font-awesome-icon :icon="['fas', 'exclamation-circle']" class="icon-exclamation-circle" />
                      Vui lòng điền đầy đủ thông tin ở bước tiếp theo để kích hoạt tài khoản nhanh hơn.</span><br>Nếu bạn đã có tài khoản, vui lòng <a href="/sign-in">Đăng nhập</a>.
                  </p>
                </b-col>

                <div class="form-group">
                  <b-button type="submit" variant="warning" class="btn btn-block">
                    <font-awesome-icon :icon="['fas', 'user']"/> Tạo tài khoản
                  </b-button>
                </div>
              </b-row>
              <b-row class="ml-1">
                <router-link to="/sign-in" class="go-back">
                  <span><font-awesome-icon :icon="['fas', 'less-than']"/> Quay lại</span>
                </router-link>
              </b-row>
            </b-form>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<style lang="scss">
  .top-nav-thuocsi-logo {
    left: 30px;
    display: flex;
    position: relative;
    height: 100%;
  }

  .top-nav-contact-us {
    display: flex;
    align-items: center;
    right: 30px;
  }

  .card-login-form {
    border: 1px solid #00b46e;;
    background: #fff;
    top: 6em;
    position: relative;
  }

  .login-title {
    color: #00b46e;;
    margin-bottom: 1.5rem;
    font-weight: normal;
    text-align: center;
  }

  .logo {
    width: 10em;
  }

  .header-right {
    display: flex;
    justify-content: flex-end;
  }

  .icon-phone-square {
    font-size: 2rem;
    margin-right: 5px;
    color: #00b46e;;
  }

  .contact-us-text {
    color: #00b46e;
    text-decoration: none;
    background-color: transparent;
  }

  .go-back {
    color: #00b46e;;
  }
</style>

<script>
export default {
  data() {
    return {
      form: {
        email: "",
        password: "",
        checked: []
      },
      show: true
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();

      this.form.email = "";
      this.form.password = "";
      this.form.checked = [];
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  }
}
</script>