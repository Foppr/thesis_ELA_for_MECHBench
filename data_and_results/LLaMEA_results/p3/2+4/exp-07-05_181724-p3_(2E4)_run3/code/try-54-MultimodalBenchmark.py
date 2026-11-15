import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base with conditioning
        quadratic = np.sum(x_norm**2)
        
        # Chaotic saddle point component using tent map
        chaotic = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                chaotic += np.abs(x_norm[i] + x_norm[i+1] - 1.0) * np.abs(x_norm[i] - x_norm[i+1])
        
        # Embedded Gaussian mixture components with varying covariances
        gauss_mixture = 0.0
        for i in range(5):
            mean = np.sin(i * np.pi / 5.0) * np.ones(self.dim)
            cov = np.eye(self.dim) * (0.5 + i * 0.1)
            diff = x_norm - mean
            gauss_mixture += np.exp(-0.5 * np.dot(diff, np.linalg.solve(cov, diff)))
        
        # Fractional Brownian motion approximation using Hurst parameter
        fbm = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                fbm += (x_norm[i+1] - x_norm[i])**2 * (i + 1)**(-0.3)
        
        # Trigonometric polynomial with variable frequency
        trig_poly = 0.0
        for i in range(1, 6):
            trig_poly += np.sin(i * np.pi * x_norm).sum() * (0.1 * i)
        
        # Polynomial with negative exponents (creating plateaus)
        poly_neg = np.sum(1.0 / (1.0 + np.abs(x_norm)**0.5))
        
        # Radial basis with dynamic width
        rbf_dynamic = 0.0
        for i in range(1, self.dim + 1):
            rbf_dynamic += np.exp(-i * x_norm**2)
        
        # Cross-term interactions with asymmetric coupling
        cross_terms = 0.0
        for i in range(self.dim - 1):
            cross_terms += x_norm[i] * x_norm[i+1] * (x_norm[i] + x_norm[i+1])**2
        
        # Add noise for non-triviality
        noise = 0.001 * np.random.random()
        
        # Combine all components with weights
        return (0.2 * quadratic + 
                0.2 * chaotic + 
                0.15 * gauss_mixture + 
                0.1 * fbm + 
                0.1 * trig_poly + 
                0.08 * poly_neg + 
                0.07 * rbf_dynamic + 
                0.05 * cross_terms + 
                noise)