import numpy as np

class FractalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic component with varying r parameters
        chaotic_term = 0.0
        r_values = np.linspace(3.5, 4.0, self.dim)
        x_prev = 0.5 * np.ones(self.dim)
        for _ in range(100):  # Burn-in period
            x_prev = r_values * x_prev * (1 - x_prev)
        for i in range(self.dim):
            x_prev[i] = r_values[i] * x_prev[i] * (1 - x_prev[i])
            chaotic_term += np.sin(x_prev[i] * np.pi) ** 2
        
        # Radial basis function component with varying widths and centers
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 20)
        widths = np.logspace(-1, 1, 20)
        for i, (center, width) in enumerate(zip(centers, widths)):
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # Fractal Brownian motion component using midpoint displacement
        fbm_term = 0.0
        for i in range(self.dim):
            fbm_term += np.sin(2.0**(i+1) * x[i]) * (2.0**(-i-1))
        
        # Multiscale sinusoidal interference pattern
        interference_term = 0.0
        frequencies = np.logspace(0, 3, 10)
        for freq in frequencies:
            interference_term += np.sin(freq * x) * np.cos(freq * x)
        
        # Polynomial distortion with fractional exponents and random coefficients
        poly_term = np.sum((x**1.7 + 0.5 * x**2.3 - 0.8 * x**1.1 + 1.2 * x + 0.6)**1.3)
        
        # Cross-term interaction with varying coupling strengths
        cross_term = 0.0
        for i in range(self.dim-1):
            cross_term += (x[i] * x[i+1]) * np.sin(0.5 * (x[i] + x[i+1]))
        
        # Gaussian modulation with adaptive width based on coordinate values
        gauss_term = 0.0
        for i in range(self.dim):
            width = 0.5 + 0.5 * np.abs(x[i])
            gauss_term += np.exp(-0.5 * (x[i]**2) / width**2) * np.cos(3.0 * x[i])
        
        # Hyperbolic tangent distortion to create sharp transitions
        tanh_distort = np.sum(np.tanh(x)**2)
        
        # Global scaling and offset to balance contributions
        return 0.15 * chaotic_term + 0.20 * rbf_term + 0.12 * fbm_term + 0.10 * interference_term + 0.15 * poly_term + 0.08 * cross_term + 0.08 * gauss_term + 0.12 * tanh_distort + 3.0