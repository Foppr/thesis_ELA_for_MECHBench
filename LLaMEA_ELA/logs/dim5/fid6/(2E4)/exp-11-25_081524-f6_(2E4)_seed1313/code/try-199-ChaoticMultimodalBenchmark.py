import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.03
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient with fractal-like basin boundaries and time-varying frequency
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.8 * np.sin(0.4 * self.t + i * 0.7) + 0.5 * np.cos(0.6 * self.t + i * 0.3)
            amp = 1.2 + 0.7 * np.sin(0.5 * self.t + i * 0.4) * np.cos(0.3 * self.t + i * 0.6)
            chaotic_grad += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) + 0.15 * x[i]**6
        
        # Multi-resolution harmonic interference with dynamic phase shifts and fractal coupling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+12, self.dim)):
                phase = 0.3 * np.sin(0.5 * self.t + i * 0.4 + j * 0.3) + 0.2 * np.cos(0.7 * self.t + i * 0.2 + j * 0.5)
                dist = np.sqrt((x[i] - x[j])**2 + 0.001)
                coupling += np.exp(-dist**3) * np.sin(3.0 * dist + phase) * (1.0 + 0.15 * np.sin(0.6 * self.t + i + j))
        
        # Adaptive penalty with fractal-like boundary interactions and higher-order terms
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.2:
                penalty += 15.0 * (abs(x[i]) - 4.2)**2 + 3.0 * (abs(x[i]) - 4.2)**4 + 0.5 * (abs(x[i]) - 4.2)**6
            elif abs(x[i]) < 0.2:
                penalty += 8.0 * (0.2 - abs(x[i]))**2 + 2.0 * (0.2 - abs(x[i]))**4
        
        # Higher-order polynomial interactions with multi-resolution harmonic scaling
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+10, self.dim)):
                poly_interaction += (x[i]**3 + x[j]**3) * np.sin(0.4 * self.t + i * 0.5 + j * 0.4) * (1.0 + 0.2 * np.cos(self.t))
        
        # Dynamic weights with fractal-like scaling and time-varying components
        w1 = 0.4 + 0.2 * np.sin(0.7 * self.t + 0.5)
        w2 = 0.35 + 0.25 * np.cos(0.6 * self.t + 0.3)
        w3 = 0.2 + 0.15 * np.sin(0.8 * self.t + 0.7)
        w4 = 0.35 + 0.2 * np.cos(0.5 * self.t + 0.2)
        
        # Combine all components with fractal scaling
        result = w1 * chaotic_grad + w2 * coupling + w3 * poly_interaction + w4 * penalty
        
        # Apply fractal dimensionality-dependent scaling factor
        if self.dim > 1:
            scale_factor = 1.0 + 0.15 * np.log(self.dim) + 0.02 * self.dim**0.9 + 0.005 * np.sin(0.3 * self.t)
            result *= scale_factor
            
        return result