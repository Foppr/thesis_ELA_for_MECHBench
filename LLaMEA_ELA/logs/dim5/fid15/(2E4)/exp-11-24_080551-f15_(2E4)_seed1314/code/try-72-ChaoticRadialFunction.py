import numpy as np

class ChaoticRadialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base radial basis function with dynamic widths and shifted centers
        result = 0.0
        for i in range(self.dim):
            width = 1.2 + 0.6 * np.cos(i * 1.5)
            center = np.sin(i * 2.1) * 1.8
            result += np.exp(-np.sum((x - center)**2) / (2.0 * width**2))
            
        # Enhanced chaotic sine coupling with multiple modulation frequencies
        for i in range(self.dim):
            freq1 = 2.8 * (i + 1)
            freq2 = 1.8 * np.pi * (i + 1) * np.sin(i * 0.7)
            chaotic_factor = np.sin(freq1 * x[i]) + 0.4 * np.sin(freq2 * x[i])
            result += 0.6 * np.sin(2.5 * x[i] + chaotic_factor) * np.cos(2.5 * x[i] - chaotic_factor)
            
        # Multi-scale adaptive penalty with exponential and polynomial components
        dist = np.sqrt(np.sum(x**2))
        penalty = 2.5 * dist * np.exp(-dist / 3.5) * (1.0 + 0.15 * np.sin(dist)) + 0.4 * dist**2
        result += penalty
        
        # Cross-dimensional interaction with varying coupling strengths and phase shifts
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.35 * (i + 1) / (j + 1)
                phase_shift = np.sin(i * j * 0.4)
                result += strength * np.sin(x[i] * x[j] + phase_shift) * np.cos(x[i] - x[j])
                
        # Multi-scale oscillatory terms with varying amplitudes and frequencies
        for i in range(self.dim):
            freq = 2.5 * (i + 1) * np.cos(i * 0.6)
            amp = 0.25 + 0.15 * np.sin(i * 1.2)
            result += amp * np.sin(freq * x[i])**3 * np.cos(freq * x[i])**3
            
        # Asymmetric basin terms with varying exponents and multipliers
        for i in range(self.dim):
            asym_term = (x[i] - 1.3)**4 + 0.6 * (x[i] + 1.3)**3
            multiplier = 0.12 * np.exp(-abs(x[i]) * 0.4)
            result += multiplier * asym_term
            
        # Central repulsion with dynamic strength and complex phase modulation
        center_dist = np.sqrt(np.sum((x - 0.6)**2))
        phase_mod = np.sin(center_dist * 1.3) + 0.25 * np.cos(center_dist * 1.8)
        result += 1.0 * np.exp(-center_dist**2 / 2.5) * phase_mod
        
        # Additional high-frequency noise component to increase ruggedness
        noise = 0.04 * np.sum(np.sin(8.0 * x)**2)
        result += noise
        
        # Higher-order polynomial interactions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.04 * (x[i]**2) * (x[j]**3) * x[k] * np.sin(i + j + k)
                    
        # Enhanced cross-dimensional coupling with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_factor = np.exp(-0.4 * (x[i] - x[j])**2)
                result += 0.25 * exp_factor * np.sin(4.0 * (x[i] + x[j]))
                
        # Additional asymmetric curvature with cubic terms
        for i in range(self.dim):
            result += 0.18 * (x[i] - 1.8)**3 * np.cos(x[i])
            
        return result