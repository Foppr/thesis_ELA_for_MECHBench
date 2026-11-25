import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal wave component with varying frequencies and amplitudes
        sin_term = np.sum(np.sin(1.0 * x) + 0.5 * np.sin(3.0 * x) + 0.3 * np.sin(7.0 * x) + 0.1 * np.sin(11.0 * x))
        
        # Polynomial distortion with non-integer exponents for irregular shaping
        poly_term = np.sum((x**2.5 + 0.8 * x**1.9 - 0.5 * x**1.3 + 1.2 * x + 0.7)**1.1)
        
        # Chaotic component using logistic map with parameter tuning for complexity
        chaotic_term = 0.0
        r = 3.95
        for i in range(self.dim):
            if i == 0:
                x_prev = x[i]
            else:
                x_prev = x[i-1]
            chaotic_term += np.sin(r * x_prev * (1 - x_prev))
        
        # Gaussian modulation to create localized peaks and valleys
        gauss_term = np.sum(np.exp(-0.5 * (x**2)) * np.cos(2.0 * x))
        
        # Radial basis function component for multi-scale landscape features
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 15)
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 0.3**2)
        
        # High-frequency interference pattern to increase complexity
        interference_term = np.sum(np.sin(25.0 * x) * np.cos(18.0 * x))
        
        # Cross-term interaction for increased complexity with novel coupling
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x[i] * x[i+1] * np.sin(x[i] + x[i+1]) * np.cos(0.5 * (x[i] - x[i+1])))
        
        # Additional quadratic distortion to enhance non-convexity
        quad_distort = np.sum(0.3 * (x**2) * np.sin(0.5 * x))
        
        # Novel dimension coupling term for increased algorithmic challenge
        coupling_term = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                coupling_term += np.sin(x[i] * x[i+1]) * np.cos(0.3 * (x[i]**2 + x[i+1]**2))
        
        # Add a global scaling factor to balance contribution of terms
        return 0.20 * sin_term + 0.18 * poly_term + 0.12 * chaotic_term + 0.15 * gauss_term + 0.12 * rbf_term + 0.10 * interference_term + 0.08 * cross_term + 0.05 * quad_distort + 0.03 * coupling_term + 2.0