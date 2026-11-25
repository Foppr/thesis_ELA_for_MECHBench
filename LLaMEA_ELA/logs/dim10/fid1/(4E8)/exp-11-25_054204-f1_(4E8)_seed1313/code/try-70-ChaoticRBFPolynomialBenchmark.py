import numpy as np

class ChaoticRBFPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute RBF centers and weights
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.rbf_weights = np.random.uniform(-1.0, 1.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component
        logistic_map = 0.0
        r = 3.9
        for i in range(self.dim):
            if i == 0:
                logistic_map += x[i] * r * (1 - x[i])
            else:
                logistic_map += x[i] * r * (1 - x[i]) * np.sin(x[i-1])
        
        # Radial basis function interpolation
        rbf = 0.0
        for i in range(self.dim):
            dist = np.sum((x - self.rbf_centers[i])**2)
            rbf += self.rbf_weights[i] * np.exp(-dist / (2 * 0.5**2))
        
        # Gradient-enhanced polynomial coupling
        poly_coupling = 0.0
        for i in range(self.dim):
            poly_coupling += x[i]**4 + x[i]**3 * np.cos(x[i]) + x[i]**2 * np.sin(x[i])
        
        # Cross-dimensional interaction with cosine modulation
        cross_interaction = 0.0
        for i in range(self.dim-1):
            cross_interaction += np.cos(2.0 * (x[i] - x[i+1])) * (x[i]**2 + x[i+1]**2)
        
        # Adaptive sigmoidal scaling component
        sig_scale = 0.0
        for i in range(self.dim):
            sig_scale += 1.0 / (1.0 + np.exp(-x[i] * (i+1) * 0.5))
        
        # Fractal-like harmonic polynomial
        fractal_harm = 0.0
        for i in range(self.dim):
            fractal_harm += np.sin((i+1) * x[i]) * np.cos((i+2) * x[i]) * (i+1)
        
        # Gaussian noise modulation
        noise_mod = np.random.normal(0, 0.05) * np.sum(np.exp(-0.5 * x**2))
        
        return logistic_map + rbf + poly_coupling + cross_interaction + sig_scale + fractal_harm + noise_mod