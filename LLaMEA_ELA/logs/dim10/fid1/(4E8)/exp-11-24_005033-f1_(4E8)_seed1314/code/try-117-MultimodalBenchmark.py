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
            
            # Multi-scale harmonic oscillations (modified frequencies)
            scale_factor = 1.0
            harmonic_sum = 0.0
            for k in range(1, 7):  # Increased to 6 scales
                scale_factor *= 0.4  # Reduced scaling factor
                harmonic_sum += scale_factor * np.sin(k * xi) * np.cos(k * xi)
            
            # Adaptive conditioning based on dimension (modified)
            condition = 1.0 + 0.5 * np.sin(0.3 * i) * np.abs(xi)  # Increased modulation
            
            # Asymmetric basin structure with fractal scaling
            asymmetry = 0.3 * np.sin(xi**2) * np.cos(0.6 * xi)  # Increased asymmetry
            
            result += condition * (base + harmonic_sum) + asymmetry
            
        # Cross-dimensional coupling with fractal scaling (modified strength)
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling strength (increased base)
                coupling_strength = 0.3 * (1 + np.cos(0.15 * (i + j)))  # Increased coupling
                distance = np.abs(x[i] - x[j])
                coupling += coupling_strength * np.sin(distance) * np.exp(-0.15 * distance**2)
                
        # Add fractal periodicity component (modified terms)
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-fractal periodic terms (different exponents)
            term = 0.0
            for k in range(1, 5):  # Increased to 4 terms
                term += np.sin(k * xi) * np.cos(k * xi) / (k**1.3)  # Changed denominator
            periodicity += term
            
        # Combine all components with different weights
        result = 0.6 * result + 0.4 * coupling + 0.25 * periodicity  # Modified weights
        
        # Fractal penalty term for distance from origin (modified exponents)
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal-like penalty with varying exponents (increased nonlinearity)
            if xi >= 0:
                penalty += 0.12 * xi**(2.5 + 0.6 * np.sin(i))  # Increased exponent
            else:
                penalty += 0.18 * np.abs(xi)**(3.5 + 0.4 * np.cos(i))  # Increased exponent
                
        result += penalty
        
        # Final scaling to ensure good fitness range
        result *= 1.7  # Increased scaling factor
        
        return result