import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal wave component with increased frequency and amplitude modulation
        sin_term = np.sum(1.2 * np.sin(1.5 * x) + 0.7 * np.sin(4.0 * x) + 0.4 * np.sin(8.0 * x) + 0.2 * np.sin(13.0 * x))
        
        # Polynomial distortion with higher-order non-integer exponents for more irregular shaping
        poly_term = np.sum((x**2.7 + 0.9 * x**2.1 - 0.6 * x**1.5 + 1.4 * x + 0.8)**1.2)
        
        # Chaotic component using tent map with optimized parameter for better complexity
        chaotic_term = 0.0
        a = 1.9   # Slight increase in chaos parameter for better sensitivity
        for i in range(self.dim):
            if i == 0:
                x_prev = x[i]
            else:
                x_prev = x[i-1]
            if x_prev < 0.5:
                chaotic_term += np.sin(a * x_prev)
            else:
                chaotic_term += np.sin(a * (1 - x_prev))
        
        # Gaussian modulation with adjusted parameters for better peak localization
        gauss_term = np.sum(np.exp(-0.4 * (x**2)) * np.cos(2.5 * x))
        
        # Radial basis function component with more diverse centers and wider spread
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 15)  # Increased number of centers for better coverage
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 0.7**2)
        
        # High-frequency interference pattern with increased complexity and reduced bias
        interference_term = np.sum(np.sin(25.0 * x) * np.cos(20.0 * x))  # Slight increase in frequencies
        
        # Cross-term interaction with modified weights for better coupling
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(x[:-1] + x[1:]) * 0.5)
        
        # Additional quadratic distortion to enhance non-convexity with modified coefficients
        quad_distort = np.sum(0.4 * (x**2) * np.sin(0.6 * x))  # Adjusted coefficient for better balance
        
        # Add a global scaling factor to balance contribution of terms and improve fitness score
        return 0.21 * sin_term + 0.18 * poly_term + 0.15 * chaotic_term + 0.13 * gauss_term + 0.12 * rbf_term + 0.10 * interference_term + 0.06 * cross_term + 0.05 * quad_distort + 1.8