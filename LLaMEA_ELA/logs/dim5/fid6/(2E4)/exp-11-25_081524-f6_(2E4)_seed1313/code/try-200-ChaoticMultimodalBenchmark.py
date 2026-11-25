import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with dynamic frequency modulation and polynomial terms
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.2 * np.sin(0.3 * self.t + i * 0.6)
            amp = 1.0 + 0.5 * np.cos(0.4 * self.t + i * 0.5)
            chaotic_grad += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) + 0.1 * x[i]**5
        
        # Dynamic coupling with sinusoidal phase shifts and exponential decay
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):
                phase = 0.2 * np.sin(0.4 * self.t + i * 0.3 + j * 0.2)
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                coupling += np.exp(-dist**2) * np.sin(2.0 * dist + phase) * (1.0 + 0.1 * np.sin(0.5 * self.t + i + j))
        
        # Adaptive penalty with quadratic and cubic terms based on distance from boundaries
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.0:
                penalty += 10.0 * (abs(x[i]) - 4.0)**2 + 2.0 * (abs(x[i]) - 4.0)**3
            elif abs(x[i]) < 0.3:
                penalty += 5.0 * (0.3 - abs(x[i]))**2 + 1.0 * (0.3 - abs(x[i]))**3
        
        # Higher-order polynomial interactions with dynamic scaling
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                poly_interaction += (x[i]**2 + x[j]**2) * np.sin(0.3 * self.t + i * 0.4 + j * 0.3) * (1.0 + 0.05 * np.cos(self.t))
        
        # Dynamic weights for combining components
        w1 = 0.35 + 0.15 * np.sin(0.6 * self.t)
        w2 = 0.4 + 0.2 * np.cos(0.5 * self.t)
        w3 = 0.25 + 0.1 * np.sin(0.7 * self.t)
        w4 = 0.3 + 0.18 * np.cos(0.4 * self.t)
        
        # Combine all components with dynamic scaling
        result = w1 * chaotic_grad + w2 * coupling + w3 * poly_interaction + w4 * penalty
        
        # Apply dimensionality-dependent scaling factor
        if self.dim > 1:
            scale_factor = 1.0 + 0.1 * np.log(self.dim) + 0.01 * self.dim**0.8
            result *= scale_factor
            
        return result