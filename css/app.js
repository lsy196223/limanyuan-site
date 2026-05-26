// 移动端菜单
function toggleMenu() {
    document.getElementById('navLinks').classList.toggle('show');
}

// 点击导航链接后关闭菜单
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        document.getElementById('navLinks').classList.remove('show');
    });
});

// 回到顶部按钮
const backToTop = document.getElementById('backToTop');
window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
        backToTop.classList.add('show');
    } else {
        backToTop.classList.remove('show');
    }
});

// 导航栏滚动阴影
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// ══════════════════════════════════════════════
//  微信二维码弹窗
// ══════════════════════════════════════════════

function showWechatModal() {
    var modal = document.getElementById('wechatModal');
    if (modal) {
        modal.classList.add('show');
        document.body.style.overflow = 'hidden';
    }
}

function closeWechatModal(event) {
    // 如果传了 event 且不是点击遮罩，忽略
    if (event && event.target !== document.getElementById('wechatModal')) return;
    var modal = document.getElementById('wechatModal');
    if (modal) {
        modal.classList.remove('show');
        document.body.style.overflow = '';
    }
}

// ESC 关闭弹窗
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeWechatModal();
});

// ══════════════════════════════════════════════
//  表单提交 → 弹出二维码
// ══════════════════════════════════════════════

function handleFormSubmit() {
    var nameEl = document.getElementById('cName');
    var phoneEl = document.getElementById('cPhone');
    var name = nameEl ? nameEl.value.trim() : '';
    var phone = phoneEl ? phoneEl.value.trim() : '';

    if (!name) { alert('请填写您的姓名'); nameEl && nameEl.focus(); return; }
    if (!phone) { alert('请填写联系电话'); phoneEl && phoneEl.focus(); return; }

    // 弹出微信二维码
    showWechatModal();

    // 清空表单
    var form = document.getElementById('contactForm');
    if (form) form.reset();
}
