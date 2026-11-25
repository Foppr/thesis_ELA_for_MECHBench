import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.a = 3.9
        self.b = 0.1
        self.c = 0.5
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic component with time-varying dynamics
        chaotic_factor = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic sine wave with dynamic frequency modulation
            freq_mod = np.sin(0.5 * (i + 1) * xi) * self.a
            chaotic_term = np.sin(freq_mod * xi) * np.cos(freq_mod * xi)
            
            # Add chaotic influence to the result
            chaotic_factor += chaotic_term
            
        # Harmonic oscillations with varying amplitudes and frequencies
        harmonic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            amp = 1.0 + 0.3 * np.sin(0.2 * i)
            freq = 1.0 + 0.5 * np.cos(0.3 * i)
            harmonic_sum += amp * np.sin(freq * xi) * np.cos(freq * xi)
            
        # Adaptive conditioning based on dimension and chaotic dynamics
        condition = 1.0 + 0.4 * np.sin(0.2 * chaotic_factor) * np.abs(xi)
        
        # Cross-dimensional coupling with chaotic interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling strength
                coupling_strength = 0.2 + 0.1 * np.sin(0.4 * (i + j))
                diff = x[i] - x[j]
                coupling += coupling_strength * np.exp(-0.5 * diff**2) * np.sin(diff)
                
        # Asymmetric basin structure with chaotic modulation
        asymmetry = 0.0
        for i in range(self.dim):
            xi = x[i]
            asymmetry += 0.2 * np.sin(xi**3) * np.cos(0.5 * xi) * np.exp(-0.1 * xi**2)
            
        # Combine all components with dynamic weights
        result = 0.7 * harmonic_sum + 0.2 * coupling + 0.1 * asymmetry
        
        # Add chaotic penalty term for distance from origin
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            penalty += 0.15 * np.abs(xi)**(2.0 + 0.3 * np.sin(i))
            
        result += penalty
        
        # Apply final chaotic scaling
        result *= 1.5 + 0.3 * np.sin(0.7 * chaotic_factor)
        
        return result