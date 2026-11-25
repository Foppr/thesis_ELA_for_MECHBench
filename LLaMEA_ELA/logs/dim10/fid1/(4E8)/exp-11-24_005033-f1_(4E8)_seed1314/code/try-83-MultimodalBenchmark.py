import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal component with recursive scaling and chaotic modulation
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic sine-cosine interactions with polynomial conditioning
            base_fractal = np.sin(3 * xi) * np.cos(7 * xi) + 0.5 * np.sin(9 * xi) * np.cos(13 * xi)
            
            # Modified polynomial conditioning with dynamic exponents
            poly_cond = (xi**4 + 0.5 * xi**2 + 0.1) / (1.0 + 0.1 * xi**2)
            
            # Adaptive gradient modulation based on neighborhood
            grad_mod = 1.0 + 0.3 * np.sin(2 * xi) * np.cos(4 * xi) * np.exp(-0.5 * np.sum(x**2))
            
            # Self-similar coupling with previous dimensions
            coupling = 0.0
            if i > 0:
                coupling = 0.2 * np.sin(x[i-1] * xi) * np.exp(-0.5 * (xi - x[i-1])**2)
            
            result += grad_mod * base_fractal * poly_cond + coupling
            
        # Enhanced gradient inversion with multi-scale deception
        gradient_inversion = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Create deceptive valleys by inverting gradients with varying scales
            scale_factor = (i + 1) * 0.5
            gradient_inversion += scale_factor * (xi**3) * np.cos(5 * xi) * np.sin(2 * xi)
            
        # Multi-scale periodicity with varying frequencies and amplitudes
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = (i + 1) * 1.5
            amp = 1.0 + 0.2 * np.sin(i)
            periodicity += amp * np.sin(freq * xi) * np.cos(freq * xi)
            
        # Cross-dimensional fractal coupling with recursive structure and quartic terms
        cross_fractal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Recursive coupling that depends on previous dimensions with quartic interactions
                cross_fractal += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2)) * \
                                np.exp(-0.1 * (x[i]**2 + x[j]**2)) * \
                                (1.0 + 0.1 * np.sin(x[i] + x[j])) * \
                                (x[i]**4 + x[j]**4)
        
        # Add quartic coupling terms for enhanced multimodality
        quartic_coupling = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                quartic_coupling += 0.05 * (xi**2 + x[j]**2)**2 * np.sin(xi * x[j])
        
        # Combine all components with different weights
        result = 0.8 * result + 0.3 * gradient_inversion + 0.4 * periodicity + 0.7 * cross_fractal + 0.5 * quartic_coupling
        
        # Add penalty for distance from origin to encourage convergence to global minimum
        result += 0.1 * np.sum(x**6) + 0.05 * np.sum(np.abs(x)**3)
        
        return result