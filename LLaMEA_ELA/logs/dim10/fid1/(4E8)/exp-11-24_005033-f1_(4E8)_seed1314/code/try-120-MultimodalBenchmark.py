import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced fractal structure with chaotic components
        for i in range(self.dim):
            xi = x[i]
            
            # Chaotic sine-wave interaction
            chaotic_component = np.sin(xi) * np.cos(3 * xi) + 0.3 * np.sin(5 * xi)
            
            # Multi-scale harmonic oscillations with varying amplitudes
            harmonic_sum = 0.0
            for k in range(1, 8):  # Increased to 7 scales for more complexity
                amplitude = 1.0 / (k**1.2)  # Decreasing amplitude
                harmonic_sum += amplitude * np.sin(k * xi) * np.cos(k * xi)
            
            # Dynamic conditioning with dimension-dependent factor
            condition_factor = 1.0 + 0.4 * np.sin(0.3 * i) * np.tanh(xi)
            
            # Asymmetric basin with enhanced nonlinearity
            asymmetry = 0.25 * np.sin(xi**2) * np.cos(0.3 * xi) + 0.1 * np.sin(xi**3)
            
            # Combine components with adaptive weights
            result += condition_factor * (chaotic_component + harmonic_sum) + asymmetry
            
        # Enhanced cross-dimensional coupling with fractal-like interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal coupling strength with exponential decay
                coupling_strength = 0.3 * np.exp(-0.1 * (i + j)) * (1 + np.cos(0.2 * (i - j)))
                distance = np.abs(x[i] - x[j])
                coupling += coupling_strength * np.sin(distance) * np.exp(-0.05 * distance**2)
                
        # Multi-fractal periodicity with enhanced complexity
        periodicity = 0.0
        for i in range(self.dim):
            xi = x[i]
            term = 0.0
            for k in range(1, 6):  # Reduced to 5 terms for better conditioning
                weight = 1.0 / (k**1.3)
                term += weight * np.sin(k * xi) * np.cos(k * xi)
            periodicity += term
            
        # Add enhanced coupling and periodicity components
        result = 0.6 * result + 0.25 * coupling + 0.15 * periodicity
        
        # Improved penalty term with better scaling
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Modified penalty with more balanced exponents
            if xi >= 0:
                penalty += 0.12 * xi**(2.5 + 0.3 * np.sin(i))
            else:
                penalty += 0.18 * np.abs(xi)**(2.8 + 0.2 * np.cos(i))
                
        result += penalty
        
        # Final scaling with improved fitness range
        result *= 1.2
        
        return result