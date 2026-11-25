import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters with higher complexity
        self.a = 4.0
        self.b = 0.15
        self.c = 0.6
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic component with quaternion-based dynamics
        chaotic_factor = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Quaternion-inspired chaotic sine wave with dynamic frequency modulation
            freq_mod = np.sin(0.5 * (i + 1) * xi) * self.a
            chaotic_term = np.sin(freq_mod * xi) * np.cos(freq_mod * xi) * np.sin(0.3 * xi**2)
            
            # Add chaotic influence to the result
            chaotic_factor += chaotic_term
            
        # Harmonic oscillations with quaternion-based amplitude modulation
        harmonic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            amp = 1.0 + 0.4 * np.sin(0.2 * i) * np.cos(0.1 * i)
            freq = 1.0 + 0.6 * np.cos(0.3 * i) * np.sin(0.2 * i)
            harmonic_sum += amp * np.sin(freq * xi) * np.cos(freq * xi) * np.exp(-0.05 * xi**2)
            
        # Adaptive conditioning with exponential scaling
        condition = 1.0 + 0.5 * np.sin(0.2 * chaotic_factor) * np.exp(-0.1 * np.abs(xi))
        
        # Cross-dimensional coupling with quaternion rotation effects
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quaternion-inspired coupling strength
                coupling_strength = 0.3 + 0.2 * np.sin(0.4 * (i + j)) * np.cos(0.3 * (i - j))
                diff = x[i] - x[j]
                coupling += coupling_strength * np.exp(-0.5 * diff**2) * np.sin(diff) * np.cos(0.1 * diff)
                
        # Asymmetric basin structure with exponential modulation
        asymmetry = 0.0
        for i in range(self.dim):
            xi = x[i]
            asymmetry += 0.3 * np.sin(xi**3) * np.cos(0.5 * xi) * np.exp(-0.1 * xi**2) * np.tanh(xi)
            
        # Novel exponential penalty structure with chaotic scaling
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            penalty += 0.2 * np.exp(0.5 * np.abs(xi)) * (1.0 + 0.1 * np.sin(i))
            
        # Combine all components with dynamic weights
        result = 0.6 * harmonic_sum + 0.25 * coupling + 0.15 * asymmetry
        
        # Add quaternion-based chaotic penalty term for distance from origin
        quat_penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            quat_penalty += 0.1 * np.abs(xi)**(2.0 + 0.4 * np.sin(i)) * np.cos(0.2 * i)
            
        result += penalty + quat_penalty
        
        # Apply final quaternion-based chaotic scaling
        result *= 1.8 + 0.4 * np.sin(0.7 * chaotic_factor) * np.cos(0.3 * chaotic_factor)
        
        return result