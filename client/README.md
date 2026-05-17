quantum-labs/
│
├── client/
│   │
│   ├── public/
│   │   ├── videos/
│   │   │   ├── hero-video.mp4
│   │   │   └── ai-bg.mp4
│   │   │
│   │   ├── images/
│   │   │   ├── logo/
│   │   │   │   ├── quantum-logo.svg
│   │   │   │   └── favicon.ico
│   │   │   │
│   │   │   ├── projects/
│   │   │   ├── services/
│   │   │   ├── team/
│   │   │   └── backgrounds/
│   │   │
│   │   ├── icons/
│   │   └── fonts/
│   │
│   ├── src/
│   │   │
│   │   ├── api/
│   │   │   ├── axios.js
│   │   │   ├── authApi.js
│   │   │   ├── serviceApi.js
│   │   │   ├── projectApi.js
│   │   │   ├── blogApi.js
│   │   │   ├── leadApi.js
│   │   │   ├── pricingApi.js
│   │   │   └── analyticsApi.js
│   │   │
│   │   ├── app/
│   │   │   ├── App.jsx
│   │   │   ├── main.jsx
│   │   │   └── providers.jsx
│   │   │
│   │   ├── assets/
│   │   │
│   │   ├── components/
│   │   │   │
│   │   │   ├── common/
│   │   │   │   ├── Button.jsx
│   │   │   │   ├── Input.jsx
│   │   │   │   ├── Textarea.jsx
│   │   │   │   ├── Modal.jsx
│   │   │   │   ├── Loader.jsx
│   │   │   │   ├── GradientBorder.jsx
│   │   │   │   ├── SectionTitle.jsx
│   │   │   │   ├── Badge.jsx
│   │   │   │   ├── Container.jsx
│   │   │   │   ├── GlowCard.jsx
│   │   │   │   └── AnimatedText.jsx
│   │   │   │
│   │   │   ├── navbar/
│   │   │   │   ├── Navbar.jsx
│   │   │   │   ├── NavLinks.jsx
│   │   │   │   ├── MegaMenu.jsx
│   │   │   │   ├── MobileMenu.jsx
│   │   │   │   ├── NavbarDropdown.jsx
│   │   │   │   └── NavbarButton.jsx
│   │   │   │
│   │   │   ├── hero/
│   │   │   │   ├── Hero.jsx
│   │   │   │   ├── HeroContent.jsx
│   │   │   │   ├── HeroVideo.jsx
│   │   │   │   ├── HeroParticles.jsx
│   │   │   │   ├── HeroStats.jsx
│   │   │   │   └── HeroButtons.jsx
│   │   │   │
│   │   │   ├── services/
│   │   │   │   ├── ServicesSection.jsx
│   │   │   │   ├── ServicesGrid.jsx
│   │   │   │   ├── ServiceCard.jsx
│   │   │   │   ├── ServiceDetails.jsx
│   │   │   │   ├── ServiceFeatures.jsx
│   │   │   │   └── ServiceCTA.jsx
│   │   │   │
│   │   │   ├── projects/
│   │   │   │   ├── ProjectsSection.jsx
│   │   │   │   ├── ProjectsGrid.jsx
│   │   │   │   ├── ProjectCard.jsx
│   │   │   │   ├── ProjectModal.jsx
│   │   │   │   ├── ProjectGallery.jsx
│   │   │   │   ├── TechStack.jsx
│   │   │   │   └── CaseStudy.jsx
│   │   │   │
│   │   │   ├── ai/
│   │   │   │   ├── AISection.jsx
│   │   │   │   ├── AutomationCards.jsx
│   │   │   │   ├── AIWorkflow.jsx
│   │   │   │   ├── AIStats.jsx
│   │   │   │   └── AIShowcase.jsx
│   │   │   │
│   │   │   ├── pricing/
│   │   │   │   ├── PricingSection.jsx
│   │   │   │   ├── PricingCard.jsx
│   │   │   │   ├── PricingToggle.jsx
│   │   │   │   ├── PricingComparison.jsx
│   │   │   │   └── EnterprisePlan.jsx
│   │   │   │
│   │   │   ├── testimonials/
│   │   │   │   ├── Testimonials.jsx
│   │   │   │   ├── TestimonialCard.jsx
│   │   │   │   └── ClientLogos.jsx
│   │   │   │
│   │   │   ├── blog/
│   │   │   │   ├── BlogGrid.jsx
│   │   │   │   ├── BlogCard.jsx
│   │   │   │   ├── BlogSidebar.jsx
│   │   │   │   ├── MarkdownRenderer.jsx
│   │   │   │   └── BlogCategories.jsx
│   │   │   │
│   │   │   ├── contact/
│   │   │   │   ├── ContactForm.jsx
│   │   │   │   ├── BudgetSelector.jsx
│   │   │   │   ├── ServiceSelector.jsx
│   │   │   │   ├── FileUpload.jsx
│   │   │   │   └── ContactInfo.jsx
│   │   │   │
│   │   │   ├── dashboard/
│   │   │   │   ├── Sidebar.jsx
│   │   │   │   ├── Topbar.jsx
│   │   │   │   ├── DashboardStats.jsx
│   │   │   │   ├── DashboardChart.jsx
│   │   │   │   ├── LeadsTable.jsx
│   │   │   │   ├── RecentProjects.jsx
│   │   │   │   └── ActivityFeed.jsx
│   │   │   │
│   │   │   ├── cms/
│   │   │   │   ├── Editor.jsx
│   │   │   │   ├── BlogEditor.jsx
│   │   │   │   ├── ProjectEditor.jsx
│   │   │   │   └── MediaLibrary.jsx
│   │   │   │
│   │   │   ├── animations/
│   │   │   │   ├── FadeUp.jsx
│   │   │   │   ├── FadeIn.jsx
│   │   │   │   ├── StaggerContainer.jsx
│   │   │   │   ├── MagneticButton.jsx
│   │   │   │   ├── FloatingGlow.jsx
│   │   │   │   ├── ScrollReveal.jsx
│   │   │   │   ├── AnimatedCounter.jsx
│   │   │   │   └── CursorGlow.jsx
│   │   │   │
│   │   │   └── footer/
│   │   │       ├── Footer.jsx
│   │   │       ├── FooterLinks.jsx
│   │   │       ├── Newsletter.jsx
│   │   │       └── SocialLinks.jsx
│   │   │
│   │   ├── config/
│   │   │   ├── env.js
│   │   │   ├── constants.js
│   │   │   ├── navigation.js
│   │   │   └── seo.js
│   │   │
│   │   ├── context/
│   │   │   ├── AuthContext.jsx
│   │   │   ├── ThemeContext.jsx
│   │   │   ├── DashboardContext.jsx
│   │   │   └── ModalContext.jsx
│   │   │
│   │   ├── hooks/
│   │   │   ├── useAuth.js
│   │   │   ├── useTheme.js
│   │   │   ├── useScroll.js
│   │   │   ├── useDebounce.js
│   │   │   ├── useWindowSize.js
│   │   │   └── useAxios.js
│   │   │
│   │   ├── layouts/
│   │   │   ├── MainLayout.jsx
│   │   │   ├── DashboardLayout.jsx
│   │   │   ├── AuthLayout.jsx
│   │   │   └── BlogLayout.jsx
│   │   │
│   │   ├── pages/
│   │   │   │
│   │   │   ├── Home.jsx
│   │   │   ├── About.jsx
│   │   │   ├── Services.jsx
│   │   │   ├── Projects.jsx
│   │   │   ├── Pricing.jsx
│   │   │   ├── Blog.jsx
│   │   │   ├── Contact.jsx
│   │   │   ├── Careers.jsx
│   │   │   ├── Privacy.jsx
│   │   │   └── Terms.jsx
│   │   │   │
│   │   │   ├── auth/
│   │   │   │   ├── Login.jsx
│   │   │   │   ├── Register.jsx
│   │   │   │   ├── ForgotPassword.jsx
│   │   │   │   ├── ResetPassword.jsx
│   │   │   │   └── VerifyEmail.jsx
│   │   │   │
│   │   │   ├── dashboard/
│   │   │   │   ├── DashboardHome.jsx
│   │   │   │   ├── Users.jsx
│   │   │   │   ├── Leads.jsx
│   │   │   │   ├── ServicesManager.jsx
│   │   │   │   ├── ProjectsManager.jsx
│   │   │   │   ├── BlogManager.jsx
│   │   │   │   ├── Analytics.jsx
│   │   │   │   ├── Billing.jsx
│   │   │   │   └── Settings.jsx
│   │   │   │
│   │   │   ├── projects/
│   │   │   │   └── ProjectDetails.jsx
│   │   │   │
│   │   │   ├── blog/
│   │   │   │   └── BlogDetails.jsx
│   │   │   │
│   │   │   └── services/
│   │   │       └── ServiceDetails.jsx
│   │   │
│   │   ├── routes/
│   │   │   ├── AppRoutes.jsx
│   │   │   ├── ProtectedRoute.jsx
│   │   │   ├── AdminRoute.jsx
│   │   │   └── PublicRoute.jsx
│   │   │
│   │   ├── services/
│   │   │   ├── authService.js
│   │   │   ├── blogService.js
│   │   │   ├── projectService.js
│   │   │   ├── leadService.js
│   │   │   ├── paymentService.js
│   │   │   └── analyticsService.js
│   │   │
│   │   ├── store/
│   │   │   ├── authStore.js
│   │   │   ├── uiStore.js
│   │   │   ├── projectStore.js
│   │   │   ├── blogStore.js
│   │   │   └── dashboardStore.js
│   │   │
│   │   ├── styles/
│   │   │   ├── globals.css
│   │   │   ├── animations.css
│   │   │   ├── scrollbar.css
│   │   │   ├── gradients.css
│   │   │   └── typography.css
│   │   │
│   │   ├── utils/
│   │   │   ├── helpers.js
│   │   │   ├── validators.js
│   │   │   ├── motion.js
│   │   │   ├── formatter.js
│   │   │   ├── storage.js
│   │   │   └── logger.js
│   │   │
│   │   └── middleware/
│   │       ├── authMiddleware.js
│   │       └── roleMiddleware.js
│   │
│   ├── .env
│   ├── .gitignore
│   ├── jsconfig.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── eslint.config.js
│   ├── package.json
│   └── README.md
│
│
├── server/
│   │
│   ├── app/
│   │   │
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── auth_routes.py
│   │   │   │   ├── user_routes.py
│   │   │   │   ├── service_routes.py
│   │   │   │   ├── project_routes.py
│   │   │   │   ├── blog_routes.py
│   │   │   │   ├── lead_routes.py
│   │   │   │   ├── analytics_routes.py
│   │   │   │   ├── payment_routes.py
│   │   │   │   ├── upload_routes.py
│   │   │   │   └── admin_routes.py
│   │   │   │
│   │   │   ├── dependencies/
│   │   │   │   ├── auth_dependency.py
│   │   │   │   └── role_dependency.py
│   │   │   │
│   │   │   └── middleware/
│   │   │       ├── auth_middleware.py
│   │   │       ├── logging_middleware.py
│   │   │       ├── rate_limit.py
│   │   │       └── security_headers.py
│   │   │
│   │   ├── config/
│   │   │   ├── database.py
│   │   │   ├── settings.py
│   │   │   ├── jwt.py
│   │   │   ├── stripe.py
│   │   │   └── cloudinary.py
│   │   │
│   │   ├── controllers/
│   │   │   ├── auth_controller.py
│   │   │   ├── user_controller.py
│   │   │   ├── service_controller.py
│   │   │   ├── project_controller.py
│   │   │   ├── blog_controller.py
│   │   │   ├── lead_controller.py
│   │   │   ├── analytics_controller.py
│   │   │   ├── payment_controller.py
│   │   │   └── upload_controller.py
│   │   │
│   │   ├── models/
│   │   │   ├── user_model.py
│   │   │   ├── role_model.py
│   │   │   ├── service_model.py
│   │   │   ├── project_model.py
│   │   │   ├── blog_model.py
│   │   │   ├── lead_model.py
│   │   │   ├── payment_model.py
│   │   │   └── analytics_model.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── auth_schema.py
│   │   │   ├── user_schema.py
│   │   │   ├── service_schema.py
│   │   │   ├── project_schema.py
│   │   │   ├── blog_schema.py
│   │   │   ├── lead_schema.py
│   │   │   ├── payment_schema.py
│   │   │   └── analytics_schema.py
│   │   │
│   │   ├── services/
│   │   │   ├── auth_service.py
│   │   │   ├── user_service.py
│   │   │   ├── service_service.py
│   │   │   ├── project_service.py
│   │   │   ├── blog_service.py
│   │   │   ├── lead_service.py
│   │   │   ├── analytics_service.py
│   │   │   ├── payment_service.py
│   │   │   └── upload_service.py
│   │   │
│   │   ├── database/
│   │   │   ├── connection.py
│   │   │   ├── base.py
│   │   │   ├── session.py
│   │   │   └── seed.py
│   │   │
│   │   ├── utils/
│   │   │   ├── hash.py
│   │   │   ├── token.py
│   │   │   ├── mail.py
│   │   │   ├── logger.py
│   │   │   ├── validators.py
│   │   │   └── response.py
│   │   │
│   │   ├── websocket/
│   │   │   └── notification_socket.py
│   │   │
│   │   ├── tasks/
│   │   │   ├── email_tasks.py
│   │   │   └── cleanup_tasks.py
│   │   │
│   │   └── main.py
│   │
│   ├── alembic/
│   │
│   ├── tests/
│   │   ├── auth_test.py
│   │   ├── project_test.py
│   │   ├── blog_test.py
│   │   └── payment_test.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── .env
│   ├── .gitignore
│   └── README.md
│
│
├── nginx/
│   ├── default.conf
│   └── nginx.conf
│
├── docker/
│   ├── frontend.Dockerfile
│   ├── backend.Dockerfile
│   └── docker-compose.yml
│
├── docs/
│   ├── api-docs.md
│   ├── deployment-guide.md
│   ├── database-schema.md
│   └── architecture.md
│
├── .github/
│   └── workflows/
│       ├── frontend.yml
│       └── backend.yml
│
├── .env
├── .gitignore
├── README.md
└── LICENSE