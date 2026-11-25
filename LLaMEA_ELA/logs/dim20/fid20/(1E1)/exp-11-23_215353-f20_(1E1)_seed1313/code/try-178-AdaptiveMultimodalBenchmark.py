import numpy as np

class AdaptiveMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with varying degrees and coefficients
        poly_term = np.sum(0.5 * x**6 + 0.3 * x**4 + 0.7 * x**2 + 0.1 * x + 1.0)
        
        # Trigonometric components with varying frequencies and amplitudes
        trig_term = np.sum(0.8 * np.sin(2.0 * x) + 0.6 * np.cos(3.0 * x) + 0.4 * np.sin(5.0 * x) + 0.2 * np.cos(7.0 * x))
        
        # Radial basis function component with adaptive width
        rbf_term = 0.0
        centers = np.linspace(-5.0, 5.0, self.dim // 2 + 1)
        for i, center in enumerate(centers):
            if i < len(centers) - 1:
                width = 0.5 * (centers[i+1] - center)
            else:
                width = 0.5
            rbf_term += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # Cross-dimensional interaction terms with varying coupling strengths
        cross_term = 0.0
        for i in range(self.dim - 1):
            cross_term += (x[i]**2 + x[i+1]**2) * np.sin(x[i] * x[i+1])
        
        # Adaptive scaling based on dimensionality
        adaptive_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Gaussian noise modulation to create fitness landscape irregularities
        noise_term = np.sum(np.exp(-0.1 * (x**2)) * np.sin(3.0 * x))
        
        # Hyperbolic tangent component for smooth transitions between regions
        tanh_term = np.sum(np.tanh(0.5 * x) * np.cos(0.8 * x))
        
        # Combined fitness with weighted contributions
        return adaptive_scale * (0.2 * poly_term + 0.3 * trig_term + 0.25 * rbf_term + 
                                0.15 * cross_term + 0.1 * noise_term + 0.05 * tanh_term + 1.5)