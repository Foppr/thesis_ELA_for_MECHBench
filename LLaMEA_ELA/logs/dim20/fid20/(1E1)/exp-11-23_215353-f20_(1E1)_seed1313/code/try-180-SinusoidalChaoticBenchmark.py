import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal wave component with higher frequency harmonics and adaptive amplitudes
        sin_term = np.sum(1.2 * np.sin(1.5 * x) + 0.8 * np.sin(4.0 * x) + 0.5 * np.sin(9.0 * x) + 0.2 * np.sin(15.0 * x) + 0.1 * np.sin(23.0 * x))
        
        # Polynomial distortion with fractional exponents and dynamic coefficients
        poly_term = np.sum((x**2.7 + 0.9 * x**2.1 - 0.6 * x**1.5 + 1.3 * x + 0.8)**1.2)
        
        # Chaotic component using a modified logistic map with variable parameter for increased complexity
        chaotic_term = 0.0
        r = 3.95  # Increased chaos parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x[i]
            else:
                x_prev = x[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev))
        
        # Gaussian modulation with multi-scale variance for localized peaks and valleys
        gauss_term = np.sum(np.exp(-0.3 * (x**2)) * np.cos(2.5 * x) + 0.5 * np.exp(-0.7 * (x**2)) * np.sin(3.0 * x))
        
        # Radial basis function component with irregular spacing and variable widths
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 15)
        widths = np.linspace(0.3, 1.2, 15)
        for i, center in enumerate(centers):
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / (widths[i]**2))
        
        # High-frequency interference pattern with phase modulation to increase complexity
        interference_term = np.sum(np.sin(30.0 * x) * np.cos(25.0 * x) + 0.3 * np.sin(40.0 * x) * np.cos(35.0 * x))
        
        # Cross-term interaction with non-linear coupling and dimension-dependent scaling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x[i] * x[i+1] * np.sin(x[i] + x[i+1]) * np.cos(0.5 * x[i] * x[i+1]))
        
        # Additional quadratic distortion with non-uniform coefficients to enhance non-convexity
        quad_distort = np.sum(0.45 * (x**2) * np.sin(0.7 * x) + 0.2 * (x**3) * np.cos(0.3 * x))
        
        # Novel dimensionally coupled term with exponential interaction
        dim_coupled_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dim_coupled_term += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(2.0 * (x[i] + x[j]))
        
        # Add a global scaling factor to balance contribution of terms
        return 0.21 * sin_term + 0.19 * poly_term + 0.15 * chaotic_term + 0.16 * gauss_term + 0.12 * rbf_term + 0.13 * interference_term + 0.08 * cross_term + 0.07 * quad_distort + 0.09 * dim_coupled_term + 2.5