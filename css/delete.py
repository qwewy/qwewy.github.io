x = """
.loader {
  position: absolute;
  top: 50%;
  left: 50%;
  margin-left: -HALFWIDTHpx;
  margin-top: -HALFWIDTHpx;
  width: 0;
  height: 0;
  visibility: initial;
  transition: all .3s ease;
  color: #fff;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 2rem;
  background-color: white;
  border-radius: 50%;
  z-index: -10
  box-shadow: 10px -5px 12.5px 3.125px rgba(0, 133, 255, 0.53), inset 2px -5px 12.5px 0px rgba(235, 255, 0, 0.54), 2px 10px 12.5px 6.25px rgba(22, 243, 3, 0.55);
}
.loader:before {
  content: "";
  display: block;
  width: FULLWIDTHpx;
  height: FULLWIDTHpx;
/*  border-radius: 40% 60% 86%;
*/  background: rgba(190, 11, 224, 0.35);
  filter: blur(5px);
  box-shadow: 10px 10px 12.5px 0px rgba(0, 133, 255, 0.53), inset -7px -5px 12.5px 0px rgba(235, 255, 0, 0.54);
  animation: spin 10s linear infinite;
   visibility: initial;
  z-index: -10

}
.loader:after {
  content: "";
  display: block;
  width: FULLWIDTHpx;
  height: FULLWIDTHpx;
/*  border-radius: 60% 50% 75%;
*/  background: rgba(235, 255, 0, 0.54);
  filter: blur(5px);
  box-shadow: -10px -12px 12.5px 0px rgba(255, 0, 0, 0.25), inset 7px -2px 12.5px 0px rgba(253, 127, 11, 0.4);
  position: absolute;
  top: 0;
  animation: spin-alt 5s linear infinite;
   visibility: initial;
  z-index: -10


}
.loader-message {
  display: block;
  text-align: center;
  vertical-align: middle;
  background: white;
/*  background: #1d1d1d;
*/  width: MINUSTENpx;
  height: MINUSTENpx;
  line-height: 190px;
/*  border-radius: 50%;
*/  border: 3px solid white;
  box-shadow: 0px 0px 10px 10px white;
  text-transform: uppercase;
  font-size: 1rem;
  font-weight: bold;
  position: absolute;
  top: 50%;
  left: 50%;
  margin: 100px;
  transform: translate(-50%, -50%);
  z-index: 0;
  letter-spacing: 7.5px;
}

@keyframes spin {
  0% {
    transform: rotate(0deg) scale(1);
  }
  50% {
    transform: rotate(180deg) scale(1.2);
  }
  100% {
    transform: rotate(360deg) scale(1);
  }
}
@keyframes spin-alt {
  0% {
    transform: rotate(0deg) scale(1);
  }
  50% {
    transform: rotate(-180deg) scale(1.2);
  }
  100% {
    transform: rotate(-360deg) scale(1);
  }
}
"""
w = 160
print(x.replace("FULLWIDTH", str(w)).replace("HALFWIDTH", str(w//2)).replace("MINUSTEN", str(w-10)))
