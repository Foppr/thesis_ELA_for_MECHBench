import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic base with logistic map modulation
        chaotic_base = 0.0
        for i in range(self.dim):
            r = 3.9 + 0.1 * np.sin(0.5 * self.t + i * 0.3)
            x_i = x[i] / 5.0
            chaotic_base += r * x_i * (1 - x_i) * x_i**2
        
        # Multi-modal trigonometric component with time-varying frequencies
        trig_component = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.4 * self.t + i * 0.2)
            amp = 1.0 + 0.5 * np.cos(0.3 * self.t + i * 0.1)
            trig_component += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Saddle point landscape with varying coupling strengths
        saddle = 0.0
        for i in range(self.dim):
            coupling = 0.5 + 0.3 * np.sin(0.6 * self.t + i * 0.4)
            if i < self.dim - 1:
                saddle += coupling * x[i] * x[i+1]
                
        # Variable condition number landscape with dynamic scaling
        condition = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 2.0 * np.sin(0.7 * self.t + i * 0.3)
            condition += cond_factor * x[i]**4
            
        # Time-varying penalty for boundary avoidance with oscillating thresholds
        penalty = 0.0
        for i in range(self.dim):
            threshold = 4.0 + 1.0 * np.sin(0.8 * self.t + i * 0.2)
            if abs(x[i]) > threshold:
                penalty += 3.0 * (abs(x[i]) - threshold)**3
                
        # Adaptive weighting scheme with chaotic modulation
        w1 = 0.25 + 0.05 * np.sin(0.9 * self.t)
        w2 = 0.35 + 0.07 * np.cos(0.8 * self.t)
        w3 = 0.20 + 0.04 * np.sin(0.6 * self.t)
        w4 = 0.20 + 0.04 * np.cos(0.7 * self.t)
        
        # Combine all components
        result = w1 * chaotic_base + w2 * trig_component + w3 * saddle + w4 * condition + penalty
        
        return result