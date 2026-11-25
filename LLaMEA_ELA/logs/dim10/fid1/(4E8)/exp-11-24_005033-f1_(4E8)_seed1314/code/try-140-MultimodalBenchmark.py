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
            condition = 1.0 + 0.35 * np.sin(0.4 * i) * np.abs(xi) + 0.18 * np.cos(0.15 * xi)
            
            # Asymmetric basin structure with fractal scaling
            asymmetry = 0.35 * np.sin(xi**2) * np.cos(0.6 * xi) + 0.09 * np.sin(3 * xi)
            
            result += condition * (base + harmonic_sum) + asymmetry
            
        # Enhanced cross-dimensional coupling with fractal scaling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Altered coupling strength
                coupling_strength = 0.35 * (1 + np.cos(0.25 * (i + j)))
                distance = np.abs(x[i] - x[j])
                coupling += coupling_strength * np.sin(distance) * np.exp(-0.25 * distance**2)
                
        # Add enhanced fractal periodicity component
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Modified multi-fractal periodic terms
            term = 0.0
            for k in range(1, 7):  # Increased frequency range
                term += np.sin(k * xi) * np.cos(k * xi) / (k**1.3)
            periodicity += term
            
        # Combine all components with different weights
        result = 0.52 * result + 0.38 * coupling + 0.22 * periodicity
        
        # Modified fractal penalty term for distance from origin
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Adjusted fractal-like penalty with varying exponents
            if xi >= 0:
                penalty += 0.18 * xi**(2.4 + 0.3 * np.sin(i))
            else:
                penalty += 0.22 * np.abs(xi)**(3.2 + 0.1 * np.cos(i))
                
        result += penalty
        
        # Final scaling to ensure good fitness range
        result *= 1.35
        
        return result