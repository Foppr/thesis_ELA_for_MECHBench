import numpy as np

class ChaoticRadialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base radial basis function with dynamic widths and shifted centers
        result = 0.0
        for i in range(self.dim):
            width = 1.5 + 0.8 * np.cos(i * 1.7)
            center = np.sin(i * 2.3) * 2.0
            result += np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            
        # Enhanced chaotic sine coupling with multiple modulation frequencies
        for i in range(self.dim):
            freq1 = 3.14159 * (i + 1)
            freq2 = 2.0 * np.pi * (i + 1) * np.sin(i)
            chaotic_factor = np.sin(freq1 * x[i]) + 0.5 * np.sin(freq2 * x[i])
            result += 0.7 * np.sin(3.0 * x[i] + chaotic_factor) * np.cos(3.0 * x[i] - chaotic_factor)
            
        # Multi-scale adaptive penalty with exponential and polynomial components
        dist = np.sqrt(np.sum(x**2))
        penalty = 3.0 * dist * np.exp(-dist / 4.0) * (1.0 + 0.2 * np.sin(dist)) + 0.5 * dist**2
        result += penalty
        
        # Cross-dimensional interaction with varying coupling strengths and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.3 * (i + 1) / (j + 1)  # Reduced coupling strength
                phase_shift = np.sin(i * j * 0.5)
                result += strength * np.sin(x[i] * x[j] + phase_shift) * np.cos(x[i] - x[j])
                
        # Multi-scale oscillatory terms with varying amplitudes and frequencies
        for i in range(self.dim):
            freq = 3.0 * (i + 1) * np.cos(i * 0.7)
            amp = 0.3 + 0.2 * np.sin(i * 1.3)
            result += amp * np.sin(freq * x[i])**4 * np.cos(freq * x[i])**2
            
        # Asymmetric basin terms with varying exponents and multipliers
        for i in range(self.dim):
            asym_term = (x[i] - 1.5)**5 + 0.7 * (x[i] + 1.5)**4
            multiplier = 0.15 * np.exp(-abs(x[i]) * 0.5)
            result += multiplier * asym_term
            
        # Central repulsion with dynamic strength and complex phase modulation
        center_dist = np.sqrt(np.sum((x - 0.7)**2))
        phase_mod = np.sin(center_dist * 1.5) + 0.3 * np.cos(center_dist * 2.0)
        result += 1.2 * np.exp(-center_dist**2 / 3.0) * phase_mod
        
        # Additional high-frequency noise component to increase ruggedness (increased noise)
        noise = 0.08 * np.sum(np.sin(10.0 * x)**2)  # Increased noise level
        result += noise
        
        return result