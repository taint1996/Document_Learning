<template>
  <div class="home">
    <header class="header-no-nav">
      <b-container>
        <b-row align-v="center">
          <b-col cols="5" sm="3">
            <b-link href="/">
              <img alt="thuocsi logo" src="../assets/images/thuocsi-logo.png" class="logo lozad img-fluid" />
            </b-link>
          </b-col>
          <b-col cols="7" sm="9" class="header-right">
            <router-link to="/sign-in" class="btn btn-warning mr-2">Đăng nhập</router-link>
            <router-link class="btn btn-success" to="/sign-up">Tạo tài khoản</router-link>
            <div class="pl-2 d-sm-flex d-none align-items-center">
              <font-awesome-icon :icon="['fas', 'phone-square']" class="icon-phone-square" />
              <span>
                <a href="tel:02862848680" class='contact-us-text'>02 862 848 680</a>
                <small class="text-dark d-block">Thời gian làm việc: (8:00 - 18:00, T2 - T7)</small>
              </span>
            </div>
          </b-col>
        </b-row>
      </b-container>
    </header>


    <div class="container-fluid p-0 mb-5">
      <b-carousel
        v-model="slide"
        :interval="2500"
        controls
        background="#ababab"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <!-- Text slides with image -->
        <b-carousel-slide>
          <template v-slot:img>
            <img
              class="d-block img-fluid w-100 h-100 banner-img"
              :src="require('../assets/images/homepage/banner-1.jpg')"
              alt="Image banner"
            >
          </template>
        </b-carousel-slide>

        <!-- Slides with custom text -->
        <b-carousel-slide>
          <template v-slot:img>
            <img
              class="d-block img-fluid w-100 h-100 banner-img"
              :src="require('../assets/images/homepage/banner-2.jpg')"
              alt="Image banner"
            >
          </template>
        </b-carousel-slide>

        <b-carousel-slide>
          <template v-slot:img>
            <img
              class="d-block img-fluid w-100 h-100 banner-img"
              :src="require('../assets/images/homepage/banner-new-5.jpg')"
              alt="Image banner"
            >
          </template>
        </b-carousel-slide>
      </b-carousel>
    </div>

    <footer class="footer">
      <b-container class="bv-example-row bv-example-row-flex-cols mb-4">
        <b-row align-v="top">
          <b-col cols="6">
            <b-link href="/">
              <img alt="thuocsi logo" src="../assets/images/thuocsi-logo.png" class="logo lozad img-fluid" />
            </b-link>
            <div class="mt-3"><strong>thuocsi.vn là website thuộc sở hữu của Công ty TNHH Buymed.</strong></div>
            <div class="mt-3"><strong>Công Ty TNHH Buymed</strong></div>
            <div class="mt-2">
              <b>Địa chỉ:</b>&nbsp;
              <span>28/31 Lương Thế Vinh, phường Tân Thới Hoà, quận Tân Phú, thành phố Hồ Chí Minh</span>
            </div>
            <div class="mt-2">
              <b>Số chứng nhận đăng ký kinh doanh:</b>&nbsp;
              <span>0314758651 cấp ngày 29/11/2017 tại Sở Kế Hoạch Và Đầu Tư Thành Phố Hồ Chí Minh</span>
            </div>
            <div class="mt-2 mb-3">
              <b>Số Giấy phép Sàn thương mại điện tử:</b>&nbsp;
              <span><router-link to="#" class="license-number">0314758651/KD-0368</router-link></span>
            </div>

            <b-link href="/">
              <img alt="thuocsi logo" src="../assets/images/bo-cong-thuong-red-logo.png" class="logo lozad img-fluid" />
            </b-link>
          </b-col>

          <b-col cols="6">
            <b-row>
              <b-col cols="6" class="p-0">
                <b-col cols="12">
                  <h5 class="footer-title-header">THÔNG TIN CHUNG</h5>

                  <div class="mb-2"
                    v-for="url in generalInformations"
                    v-bind:key="url">
                    <router-link to="#" class="footer-link">
                      {{ url.titleUrl }}
                    </router-link>
                  </div>
                </b-col>
              </b-col>

              <b-col cols="6" class="p-0 col-offset-6">
                <b-col cols="12">
                  <h5 class="footer-title-header">Liên hệ</h5>

                  <div class="d-flex mb-2">
                    <span>
                      <font-awesome-icon :icon="['fas', 'envelope']" class="mr-2" />
                      <a href="mailto:hotro@thuocsi.vn" class="footer-link">hotro@thuocsi.vn</a>
                    </span>
                  </div>

                  <div class="d-flex">
                    <font-awesome-icon :icon="['fas', 'phone']" class="mr-2" />
                    <span>
                      <a href="tel:02862848680" class="footer-link">02 862 848 680</a>
                      <br>
                      <small>(8:00 - 18:00, T2 - T7)</small>
                    </span>
                  </div>
                </b-col>
              </b-col>

              <b-col cols="12">
                <h5 class="footer-title-header">Hỗ trợ khách hàng</h5>
                <router-link to="#" class="text-white">
                  Hướng dẫn đặt hàng
                </router-link>
              </b-col>
              <b-col cols="12">
                <h5 class="footer-title-header">Dịch vụ giao hàng</h5>

                <img alt="Giao hàng tiết kiệm" src="../assets/images/homepage/delivery/ghtk.png" class="footer-delivery lozad img-fluid" />
                <img alt="Ahamove" src="../assets/images/homepage/delivery/ahamove.png" class="footer-delivery lozad img-fluid" />
                <img alt="Grab" src="../assets/images/homepage/delivery/grab.png" class="footer-delivery lozad img-fluid" />
                <b-link to="#">
                  <img alt="MedX" src="../assets/images/homepage/delivery/medx.png" class="footer-delivery lozad img-fluid" />
                </b-link>
              </b-col>
            </b-row>
          </b-col>
        </b-row>
      </b-container>

      <div class="container-fluid bg-dark text-white text-center">
        <b-row>
          <b-col cols="12" class="p-1">
            © Bản quyền thuộc Công Ty TNHH Buymed - 2019
          </b-col>
        </b-row>
      </div>
    </footer>
  </div>
</template>

<style scoped lang="scss">
  $green: #00b46e;
  .logo {
    width: 10em;
  }

  .footer {
    clear: both;
    position: absolute;
    left: 0;
    bottom: 0;
    background: #343a40;
    color: #fff;
    width: 100%;
    padding-top: 2rem;
    margin-top: auto;

    &-link {
      color: #fff;
    }

    &-link:hover {
      color: $green;
      transition: color 0.2s;
    }
  }

  .header-right {
    display: flex;
    justify-content: flex-end;
  }

  .footer-title-header {
    background: linear-gradient(to right, #00b46e, #f9b514);
    text-transform: uppercase;
    font-weight: 700;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    -webkit-box-decoration-break: clone;
    box-decoration-break: clone;
  }

  .footer-delivery {
    background: #fff;
    height: 2.5rem;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
    padding: 0.5rem;
    border-radius: 3px;
    vertical-align: top;
  }

  .banner-img {
    height: 550px !important;
  }

  .license-number {
    color: #fff;
    text-decoration: underline;
  }

  .license-number:hover{
    color: $green;
    transition: color 0.2s;
  }
</style>

<script>
import axios from "axios";
import { Carousel, Slide } from 'vue-carousel';

export default {
  name: "home",
  components: {
    Carousel, Slide
  },
  data() {
    return {
      generalInformations: [
        { titleUrl: "Giới thiệu về thuocsi" },
        { titleUrl: "Câu hỏi thường gặp (Q&A)" },
        { titleUrl: "Điều khoản sử dụng" },
        { titleUrl: "Thỏa thuận về dịch vụ TMDT" },
        { titleUrl: "Quy chế hoạt động" },
        { titleUrl: "Chính sách bảo mật" },
        { titleUrl: "Cơ chế giải quyết tranh chấp" },
        { titleUrl: "Chính sách quy định chung" },
        { titleUrl: "Đăng ký bán hàng cùng thuocsi" }
      ],

      results: [],
      slide: 0,
      sliding: null
    }
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true
    },
    onSlideEnd(slide) {
      this.sliding = false
    }
  },
  mounted() {
    axios.get("https://jsonplaceholder.typicode.com/posts")
    .then(response => {
      this.results = response.data;
    }).catch(error => {
      console.log(`error result: ${error}`);
    })
  }
};
</script>
