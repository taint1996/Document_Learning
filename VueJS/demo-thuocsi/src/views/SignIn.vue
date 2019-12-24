<template>
  <div class="sign-in-form">
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
            <h3 class="mb-4 login-title">Chào mừng quay trở lại</h3>

            <b-form @submit="onSubmit" @reset="onReset" v-if="show">
              <b-form-group
                id="input-group-1"
                label="Số điện thoại hay email:"
                label-for="input-1"
              >
                <b-form-input
                  id="input-1"
                  v-model="form.email"
                  type="email"
                  required
                  placeholder="Vui lòng nhập số điện thoại hoặc email"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="input-group-2"
                label="Mật khẩu"
                label-for="input-2"
              >
                <b-form-input
                  id="input-2"
                  v-model="form.password"
                  required
                  type="password"
                  placeholder="Vui lòng nhập mật khẩu"
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-4">
                <b-form-checkbox-group v-model="form.checked" id="checkboxes-4">
                  <b-form-checkbox value="remember">
                    Nhớ mật khẩu
                  </b-form-checkbox>
                </b-form-checkbox-group>
              </b-form-group>

              <div class="form-group">
                <b-button type="submit" variant="warning" class="btn btn-secondary btn-block">
                  <div>
                    <font-awesome-icon :icon="['fas', 'sign-in-alt']"/>&nbsp;
                    <span>Đăng nhập</span>
                  </div>
                </b-button>
              </div>

              <div>
                <router-link to="forgot-password">Quên mật khẩu ?</router-link>
              </div>

              <hr>

              <div class="form-group">
                <router-link to="/sign-up" class="btn btn-block btn-success">
                  <div>
                    <font-awesome-icon :icon="['fas', 'user']"/>&nbsp;
                    <span>Tạo tài khoản</span>
                  </div>
                </router-link>
                <b-button type="button" variant="info" class="btn btn-block">
                  <div>
                    <font-awesome-icon :icon="['fas', 'eye']"/>&nbsp;
                    <span>Dùng thử</span>
                  </div>
                </b-button>
              </div>
            </b-form>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<style scoped lang="scss">
  $green: #00b46e;

  .sign-in-form {
    text-align: left;
  }

  .header-no-nav {
    padding: 1rem;
  }

  .top-nav-thuocsi-logo {
    left: 30px;
    display: flex;
    position: relative;
    height: 100%;
  }

  .top-nav-contact-us {
    display: flex;
    align-items: center;
  }

  .card-login-form {
    border: 1px solid $green;
    top: 6em;
    position: relative;
  }

  .login-title {
    color: $green;
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
    color: $green;
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
