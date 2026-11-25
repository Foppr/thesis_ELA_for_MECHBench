import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.015
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic gradient with multiple frequency components and higher-order terms
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq1 = 2.5 + 1.5 * np.sin(0.35 * self.t + i * 0.7)
            freq2 = 1.8 + 0.8 * np.cos(0.4 * self.t + i * 0.6)
            amp1 = 1.2 + 0.6 * np.sin(0.5 * self.t + i * 0.4)
            amp2 = 0.8 + 0.4 * np.cos(0.3 * self.t + i * 0.5)
            chaotic_grad += amp1 * np.sin(freq1 * x[i]) * np.cos(freq1 * x[i]) + \
                           amp2 * np.sin(freq2 * x[i]**2) * np.cos(freq2 * x[i]**2) + \
                           0.15 * x[i]**6
        
        # Enhanced dynamic coupling with multiple phase shifts and interaction terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+10, self.dim)):
                phase1 = 0.3 * np.sin(0.45 * self.t + i * 0.35 + j * 0.25)
                phase2 = 0.2 * np.cos(0.5 * self.t + i * 0.4 + j * 0.3)
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                coupling += np.exp(-dist**2.5) * (np.sin(2.5 * dist + phase1) + 0.5 * np.cos(1.5 * dist + phase2)) * \
                          (1.0 + 0.15 * np.sin(0.6 * self.t + i + j))
        
        # Modified adaptive penalty with more aggressive boundary effects
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.2:
                penalty += 15.0 * (abs(x[i]) - 4.2)**2.5 + 3.0 * (abs(x[i]) - 4.2)**4
            elif abs(x[i]) < 0.25:
                penalty += 8.0 * (0.25 - abs(x[i]))**2.5 + 1.5 * (0.25 - abs(x[i]))**4
        
        # Enhanced polynomial interactions with dynamic coupling and multi-scale terms
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):
                poly_interaction += (x[i]**3 + x[j]**3) * np.sin(0.35 * self.t + i * 0.45 + j * 0.35) * \
                                  (1.0 + 0.12 * np.cos(self.t) + 0.08 * np.sin(2 * self.t))
        
        # Dynamic weights with more complex modulation
        w1 = 0.4 + 0.2 * np.sin(0.65 * self.t + 0.5)
        w2 = 0.35 + 0.18 * np.cos(0.55 * self.t + 0.3)
        w3 = 0.2 + 0.12 * np.sin(0.75 * self.t + 0.7)
        w4 = 0.35 + 0.15 * np.cos(0.45 * self.t + 0.2)
        
        # Combine all components with enhanced scaling
        result = w1 * chaotic_grad + w2 * coupling + w3 * poly_interaction + w4 * penalty
        
        # Apply more aggressive dimensionality-dependent scaling factor
        if self.dim > 1:
            scale_factor = 1.0 + 0.15 * np.log(self.dim) + 0.02 * self.dim**0.9
            result *= scale_factor
            
        return result