page('/', todoManager.listAll);
page('/todo/create', todoManager.create);
page('/todo/:id', todoManager.listOne);

page('/login', authManager.showLogin);
page('/register', authManager.showRegister);

page({});
