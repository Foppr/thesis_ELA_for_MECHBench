import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Fractal-like structure with recursive components
        for i in range(self.dim):
            xi = x[i]
            
            # Base fractal component with self-similarity
            base = np.sin(xi) * np.cos(2 * xi) + 0.5 * np.sin(3 * xi)
            
            # Multi-scale harmonic oscillations
            scale_factor = 1.0
            harmonic_sum = 0.0
            for k in range(1, 6):  # Up to 5 scales
                scale_factor *= 0.5
                harmonic_sum += scale_factor * np.sin(k * xi) * np.cos(k * xi)
            
            # Enhanced adaptive conditioning based on dimension and position
            condition = 1.0 + 0.4 * np.sin(0.3 * i) * np.abs(xi) + 0.1 * np.cos(0.1 * xi)
            
            # Asymmetric basin structure with fractal scaling
            asymmetry = 0.25 * np.sin(xi**2) * np.cos(0.5 * xi) + 0.05 * np.sin(3 * xi)
            
            result += condition * (base + harmonic_sum) + asymmetry
            
        # Enhanced cross-dimensional coupling with fractal scaling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced fractal coupling strength
                coupling_strength = 0.3 * (1 + np.cos(0.15 * (i + j)))
                distance = np.abs(x[i] - x[j])
                coupling += coupling_strength * np.sin(distance) * np.exp(-0.15 * distance**2)
                
        # Add enhanced fractal periodicity component
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced multi-fractal periodic terms
            term = 0.0
            for k in range(1, 5):
                term += np.sin(k * xi) * np.cos(k * xi) / (k**1.3)
            periodicity += term
            
        # Combine all components with different weights
        result = 0.6 * result + 0.4 * coupling + 0.25 * periodicity
        
        # Enhanced fractal penalty term for distance from origin
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Enhanced fractal-like penalty with varying exponents
            if xi >= 0:
                penalty += 0.12 * xi**(2.2 + 0.4 * np.sin(i))
            else:
                penalty += 0.18 * np.abs(xi)**(3.2 + 0.2 * np.cos(i))
                
        result += penalty
        
        # Final scaling to ensure good fitness range
        result *= 1.3
        
        return result