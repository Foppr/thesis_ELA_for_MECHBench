import numpy as np

class MultiModalRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for consistent conditioning
        x_scaled = x / 5.0
        
        # Polynomial landscape with mixed degrees and chaotic coefficients
        f1 = np.sum(0.8 * x_scaled**6 + 0.4 * x_scaled**5 - 0.3 * x_scaled**4 + 0.2 * x_scaled**3 + 0.1 * x_scaled**2 + 0.05 * x_scaled)
        
        # Chaotic trigonometric interference creating highly complex local minima
        f2 = np.sum(np.sin(25 * x_scaled) * np.cos(22 * x_scaled) * 
                   np.sin(18 * x_scaled) * np.cos(14 * x_scaled) * 
                   np.sin(10 * x_scaled) * np.cos(8 * x_scaled))
        
        # Fractal-like radial basis function components with self-similar centers and widths
        f3 = 0.0
        for i in range(min(7, self.dim)):
            center = np.sin(i * 1.234) * 0.6 + np.cos(i * 0.567) * 0.3
            width = 0.3 + 0.1 * np.sin(i * 0.891) * np.cos(i * 0.456)
            f3 += np.exp(-0.5 * ((x_scaled[i] - center) / width)**3)
        
        # Non-linear cross-dimensional interaction terms with fractal-like coupling
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(i * j * 0.789) * np.cos(i + j * 0.321)
                f4 += coupling * (np.sin(x_scaled[i]) * np.cos(x_scaled[j]) + 
                                x_scaled[i]**3 * x_scaled[j]**2 + 
                                x_scaled[i] * x_scaled[j]**3)
        
        # Asymmetric saddle point structure with fractal exponent
        f5 = np.sum((x_scaled**2 - 0.3)**5)
        
        # Ultra-high-frequency oscillation to increase ruggedness exponentially
        f6 = np.sum(np.sin(100 * x_scaled) * np.cos(95 * x_scaled) * 
                   np.sin(90 * x_scaled) * np.cos(85 * x_scaled))
        
        # Combined penalty for boundary avoidance with fractal exponents
        f7 = 0.8 * np.sum(np.abs(x_scaled)**4.2 + np.abs(x_scaled)**2.7)
        
        # Add a chaotic noise component to make the landscape even more rugged
        noise = np.sum(0.1 * np.sin(50 * x_scaled) * np.cos(45 * x_scaled) * 
                      np.sin(40 * x_scaled) * np.cos(35 * x_scaled))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + noise