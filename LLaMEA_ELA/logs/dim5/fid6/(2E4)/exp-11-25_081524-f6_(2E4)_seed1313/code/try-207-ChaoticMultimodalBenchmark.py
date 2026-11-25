import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient with modified frequency modulation and higher-order terms
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = 1.8 + 2.0 * np.sin(0.4 * self.t + i * 0.75)
            amp = 0.9 + 0.5 * np.cos(0.5 * self.t + i * 0.6)
            chaotic_grad += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) + 0.2 * x[i]**6
        
        # Modified coupling with stronger harmonic interference and dynamic phase shifts
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                phase = 0.4 * np.sin(0.6 * self.t + i * 0.45 + j * 0.35)
                dist = np.sqrt((x[i] - x[j])**2 + 0.008)
                coupling += np.exp(-dist**2.0) * np.sin(3.0 * dist + phase) * (1.0 + 0.2 * np.sin(0.7 * self.t + i + j))
        
        # Enhanced penalty with asymmetric quadratic and quartic terms
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.1:
                penalty += 18.0 * (abs(x[i]) - 4.1)**2 + 4.0 * (abs(x[i]) - 4.1)**4
            elif abs(x[i]) < 0.3:
                penalty += 9.0 * (0.3 - abs(x[i]))**2 + 2.0 * (0.3 - abs(x[i]))**4
        
        # Increased polynomial interactions with stronger coupling and dynamic scaling
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                poly_interaction += (x[i]**4 + x[j]**4) * np.sin(0.5 * self.t + i * 0.6 + j * 0.5) * (1.0 + 0.15 * np.cos(self.t))
        
        # Dynamic weights with more complex modulation
        w1 = 0.35 + 0.25 * np.sin(0.8 * self.t)
        w2 = 0.4 + 0.2 * np.cos(0.7 * self.t)
        w3 = 0.25 + 0.1 * np.sin(0.9 * self.t)
        w4 = 0.3 + 0.25 * np.cos(0.6 * self.t)
        
        # Combine all components with dynamic scaling
        result = w1 * chaotic_grad + w2 * coupling + w3 * poly_interaction + w4 * penalty
        
        # Apply enhanced dimensionality-dependent scaling factor
        if self.dim > 1:
            scale_factor = 1.0 + 0.2 * np.log(self.dim) + 0.025 * self.dim**0.95
            result *= scale_factor
            
        return result