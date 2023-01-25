import{_ as g,r as h,o as a,c as u,F as M,e as S,f as l,g as v,a as n,n as f,h as _,t as d,i as $,j as C,p as w,d as b}from"./index-d39f5865.js";const N={name:"Menu",data(){return{aList:[{name:"Home",url:"/home",submenu:[]},{name:"User",url:"/home/user",submenu:[{name:"Document",url:"/home/document"},{name:"Folder",url:"/home/folder"},{name:"File",url:"/home/file"}]},{name:"Document",url:"/home/document",submenu:[]},{name:"Folder",url:"/home/folder",submenu:[]},{name:"Upload",url:"/upload",submenu:[]},{name:"Assignment",url:"/assignment",submenu:[]}],aStylist:["fa-home fa-lg","fa-user fa-lg","fa-shopping-basket","fa-list-alt","fa-gear fa-lg","fa-key fa-lg","fa-newspaper-o","fa-address-card-o","fa-truck fa-lg"],aNowMenu:[0,0]}},methods:{fnSetMenu:function(e){this.aNowMenu=[e[0],e[1]]},fnResetMenu:function(e){e=="/home"&&this.fnSetMenu([0,0]),e=="/home/user"&&this.fnSetMenu([1,0]),e=="/home/author"&&this.fnSetMenu([4,0]),e=="/home/group"&&this.fnSetMenu([4,1]),e=="/home/admin"&&this.fnSetMenu([4,2]),e=="/home/sku"&&this.fnSetMenu([2,0]),e=="/home/spu"&&this.fnSetMenu([2,1]),e=="/home/spuadd"&&this.fnSetMenu([2,1]),e=="/home/spuedit"&&this.fnSetMenu([2,1]),e=="/home/specs"&&this.fnSetMenu([2,2]),e=="/home/options"&&this.fnSetMenu([2,3]),e=="/home/channels"&&this.fnSetMenu([2,4]),e=="/home/brands"&&this.fnSetMenu([2,5]),e=="/home/pictures"&&this.fnSetMenu([2,6]),e=="/home/order"&&this.fnSetMenu([3,0]),e=="/home/order_detail"&&this.fnSetMenu([3,0])}},watch:{$route(e,i){this.fnResetMenu(e.path)}},mounted(){var e=this.$route.path;this.fnResetMenu(e)}},x=e=>(w("data-v-fcc861fc"),e=e(),b(),e),I={class:"menu"},F=["onClick"],H=["onClick"],L=x(()=>n("i",{class:"fa fa-circle-o"},null,-1));function V(e,i,k,y,t,c){const r=h("router-link");return a(),u("ul",I,[(a(!0),u(M,null,S(t.aList,(s,o)=>(a(),u("li",{onClick:m=>c.fnSetMenu([o,-1])},[l(r,{to:s.url,class:f(["level1",o==t.aNowMenu[0]?"current":""])},{default:v(()=>[n("i",{class:f(["fa",t.aStylist[o]])},null,2),_(d(s.name),1)]),_:2},1032,["to","class"]),s.submenu.length>0?(a(),u("ul",{key:0,class:f(o==t.aNowMenu[0]?"current"+s.submenu.length:"")},[(a(!0),u(M,null,S(s.submenu,(m,p)=>(a(),u("li",{onClick:$(T=>c.fnSetMenu([o,p]),["stop"])},[l(r,{to:m.url,class:f(p==t.aNowMenu[1]?"active":"")},{default:v(()=>[L,_(d(m.name),1)]),_:2},1032,["to","class"])],8,H))),256))],2)):C("",!0)],8,F))),256))])}const B=g(N,[["render",V],["__scopeId","data-v-fcc861fc"]]);const D={name:"Home",data(){return{username:localStorage.username}},components:{Menu:B},mounted(){},methods:{fnQuit:function(){sessionStorage.clear(),localStorage.clear(),this.$router.push({path:"/"})}}},Q=e=>(w("data-v-595b4ee8"),e=e(),b(),e),R={class:"home_wrap"},U={class:"header"},j=Q(()=>n("i",{class:"fa fa-power-off"},null,-1)),q={class:"user_info"},z={class:"side_bar"},A={class:"main_body"};function E(e,i,k,y,t,c){const r=h("Menu"),s=h("router-view");return a(),u("div",R,[n("div",U,[n("a",{href:"javascript:;",class:"quit",onClick:i[0]||(i[0]=(...o)=>c.fnQuit&&c.fnQuit(...o))},[j,_("  Logout")]),n("div",q,[n("span",null,"welcome "+d(t.username),1)])]),n("div",z,[l(r)]),n("div",A,[l(s)])])}const J=g(D,[["render",E],["__scopeId","data-v-595b4ee8"]]);export{J as default};