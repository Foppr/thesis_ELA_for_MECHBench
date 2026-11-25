import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient with higher frequency modulation and multi-scale polynomial terms
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(0.4 * self.t + i * 0.7)
            amp = 1.2 + 0.6 * np.cos(0.5 * self.t + i * 0.6)
            chaotic_grad += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) + 0.15 * x[i]**6
        
        # Enhanced dynamic coupling with multi-modal phase shifts and adaptive decay
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+10, self.dim)):
                phase = 0.3 * np.sin(0.5 * self.t + i * 0.4 + j * 0.3)
                dist = np.sqrt((x[i] - x[j])**2 + 0.02)
                coupling += np.exp(-dist**1.5) * np.sin(3.0 * dist + phase) * (1.0 + 0.15 * np.sin(0.6 * self.t + i + j))
        
        # Modified penalty with sigmoidal boundary influence and higher-order terms
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.2:
                penalty += 15.0 * (abs(x[i]) - 4.2)**2.5 + 3.0 * (abs(x[i]) - 4.2)**4
            elif abs(x[i]) < 0.25:
                penalty += 8.0 * (0.25 - abs(x[i]))**2.5 + 1.5 * (0.25 - abs(x[i]))**4
        
        # Increased polynomial interactions with cross-dimensional coupling and dynamic phase
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):
                poly_interaction += (x[i]**3 + x[j]**3) * np.sin(0.4 * self.t + i * 0.5 + j * 0.4) * (1.0 + 0.12 * np.cos(self.t))
        
        # Dynamic weights with more complex modulation for better balance
        w1 = 0.4 + 0.2 * np.sin(0.7 * self.t)
        w2 = 0.35 + 0.18 * np.cos(0.6 * self.t)
        w3 = 0.2 + 0.12 * np.sin(0.8 * self.t)
        w4 = 0.35 + 0.2 * np.cos(0.5 * self.t)
        
        # Combine all components with dynamic scaling
        result = w1 * chaotic_grad + w2 * coupling + w3 * poly_interaction + w4 * penalty
        
        # Apply enhanced dimensionality-dependent scaling factor
        if self.dim > 1:
            scale_factor = 1.0 + 0.15 * np.log(self.dim) + 0.02 * self.dim**0.9
            result *= scale_factor
            
        return result