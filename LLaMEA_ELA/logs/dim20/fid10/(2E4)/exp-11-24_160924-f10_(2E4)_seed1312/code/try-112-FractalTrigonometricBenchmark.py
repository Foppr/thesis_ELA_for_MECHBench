import numpy as np

class FractalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal-like self-similar structure using recursive trigonometric terms
        for i in range(self.dim):
            xi = x[i]
            # Self-similar fractal component with multiple scales
            fractal_term = np.sin(xi) * np.cos(2 * xi) * np.sin(4 * xi)
            # Add scale-dependent modulation
            scale_factor = 1.0 + 0.5 * np.sin(0.3 * i) * np.cos(0.2 * i)
            result += scale_factor * fractal_term
            
        # Hybrid exponential-trigonometric components with dynamic base
        for i in range(self.dim):
            xi = x[i]
            # Exponential modulation with trigonometric base
            exp_base = 1.0 + 0.3 * np.sin(0.5 * xi)
            hybrid_term = np.exp(exp_base * xi) * np.cos(3.0 * xi)
            result += 0.7 * hybrid_term
            
        # Dynamic dimension-dependent conditioning with chaotic modulation
        for i in range(self.dim):
            xi = x[i]
            # Dimension-dependent conditioning factor with chaotic variation
            cond_factor = 1.0 + 0.4 * np.sin(0.2 * i) * np.cos(0.1 * i)
            # Add conditioning to polynomial terms
            result += cond_factor * (xi**6 - 5 * xi**4 + 6 * xi**2 - 1)
            
        # Multi-scale sinusoidal coupling with frequency modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Frequency-modulated coupling term
                freq_mod = 1.0 + 0.3 * np.sin(0.4 * (i + j))
                coupling = freq_mod * np.sin(freq_mod * (x[i] - x[j])) * np.cos(freq_mod * (x[i] + x[j]))
                result += 0.5 * coupling
                
        # Add chaotic saddle point structure with rational polynomial
        for i in range(self.dim):
            xi = x[i]
            # Rational polynomial term inducing saddle points
            numerator = xi**3 - xi
            denominator = xi**2 + 0.5 + 0.2 * np.sin(3.0 * xi)
            saddle_term = numerator / denominator
            result += 0.8 * saddle_term
            
        # Add fractal peak structure with multi-modal characteristics
        for i in range(self.dim):
            xi = x[i]
            # Multiple peaks at different locations with varying heights
            peak1 = 1.0 / (1.0 + (xi - 3.0)**2 + 0.3 * np.sin(5.0 * xi))
            peak2 = 1.0 / (1.0 + (xi + 3.0)**2 + 0.2 * np.cos(4.0 * xi))
            peak3 = 1.0 / (1.0 + (xi - 1.0)**2 + 0.1 * np.tan(2.0 * xi))
            result += 0.6 * (peak1 + peak2 + peak3)
            
        # Add dynamic penalty near global optimum with exponential decay
        global_optimum = np.ones(self.dim) * 1.5
        penalty = np.sum(np.exp(-0.5 * (x - global_optimum)**2)) + 0.4 * np.sum(np.abs(x - global_optimum)**3)
        result += penalty
        
        return result