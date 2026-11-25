import numpy as np

class SinusoidalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced sinusoidal wave component with increased frequency and amplitude modulation
        sin_term = np.sum(1.2 * np.sin(1.5 * x) + 0.7 * np.sin(4.0 * x) + 0.4 * np.sin(8.0 * x) + 0.2 * np.sin(13.0 * x))
        
        # Modified polynomial distortion with higher-order terms and non-integer exponents
        poly_term = np.sum((x**2.7 + 0.9 * x**2.1 - 0.6 * x**1.5 + 1.3 * x + 0.8)**1.2)
        
        # Chaotic component using tent map with enhanced parameter tuning for greater complexity
        chaotic_term = 0.0
        a = 1.9  # Increased chaos parameter for more complex dynamics
        for i in range(self.dim):
            if i == 0:
                x_prev = x[i]
            else:
                x_prev = x[i-1]
            if x_prev < 0.5:
                chaotic_term += np.sin(a * x_prev)
            else:
                chaotic_term += np.sin(a * (1 - x_prev))
        
        # Enhanced Gaussian modulation with wider spread for broader peak valleys
        gauss_term = np.sum(np.exp(-0.3 * (x**2)) * np.cos(2.5 * x))
        
        # Improved radial basis function component with adaptive center distribution
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, 12)  # More centers for finer granularity
        for center in centers:
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / 0.6**2)
        
        # Increased high-frequency interference pattern with altered phase relationships
        interference_term = np.sum(np.sin(25.0 * x) * np.cos(19.0 * x))  # Higher frequencies and altered ratio
        
        # Enhanced cross-term interaction with additional coupling
        cross_term = np.sum(x[:-1] * x[1:] * np.sin(x[:-1] + x[1:]) * np.cos(0.5 * (x[:-1] - x[1:])))
        
        # Strengthened quadratic distortion for greater non-convexity
        quad_distort = np.sum(0.45 * (x**2) * np.sin(0.6 * x))  # Increased coefficient
        
        # Additional harmonic component to improve landscape complexity
        harm_term = np.sum(0.3 * np.sin(6.0 * x) * np.cos(9.0 * x))
        
        # Add a global scaling factor to balance contribution of terms
        return 0.21 * sin_term + 0.18 * poly_term + 0.15 * chaotic_term + 0.14 * gauss_term + 0.12 * rbf_term + 0.12 * interference_term + 0.08 * cross_term + 0.07 * quad_distort + 0.05 * harm_term + 2.5