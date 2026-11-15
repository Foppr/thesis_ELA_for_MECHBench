import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal interactions with variable frequencies
        result += 1.2 * np.sum(np.sin(5.0 * x)**4) + 0.8 * np.sum(np.cos(6.0 * x)**4)
        
        # Increased polynomial distortion with chaotic coefficients and higher-order terms
        poly_term = 0.03 * np.sum((x**5 + 0.4 * x**7 + 0.2 * x**9) * np.sin(x**3))
        
        # Stronger cross-dimensional coupling with multi-scale interaction
        coupling = 0.4 * np.sum(np.sin(x[:-3] + x[1:-2] + x[2:-1] + x[3:]) * 
                               np.cos(x[:-3] - x[1:-2] + x[2:-1] - x[3:]) * 
                               np.sin(x[:-2] + x[1:-1]))
        
        # Enhanced chaotic perturbations with hyperbolic and trigonometric components
        chaotic = 0.2 * np.sum(np.sinh(np.exp(x**2)) * np.cos(np.log(np.abs(x) + 1e-8)) * 
                              np.tan(np.sin(x)**2))
        
        # Additional multimodal component with hybrid Gaussian and Mexican Hat peaks
        gaussian_peaks = 0.25 * np.sum(np.exp(-0.5 * (x**2 - 1)**2) * np.sin(3.0 * x)**2)
        mexican_hat = 0.15 * np.sum((2 - x**2) * np.exp(-0.5 * x**2) * np.cos(2.0 * x))
        
        # Novel hybrid peak structure with asymmetric distortions
        asymmetric = 0.1 * np.sum(np.abs(x)**3 * np.sin(x)**2 * np.cos(0.5 * x))
        
        # Combine all terms
        result = result + poly_term + coupling + chaotic + gaussian_peaks + mexican_hat + asymmetric
        
        return result