import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        base = np.sum(x**2) * 0.1
        
        # Chaotic harmonic oscillation with time-varying frequency
        chaotic_osc = 0
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(0.3 * i)
            amp = 1.0 + 0.3 * np.cos(0.4 * i)
            chaotic_osc += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2) * (1 + 0.2 * np.sin(x[i]))
            
        # Multi-scale periodic components with exponential decay
        multi_scale = 0
        for i in range(self.dim):
            scale1 = np.exp(-0.5 * (x[i] - 1.0)**2)
            scale2 = np.exp(-0.3 * (x[i] + 2.0)**2)
            scale3 = np.exp(-0.7 * (x[i] - 3.0)**2)
            multi_scale += (np.sin(3.0 * x[i]) * scale1 + 
                           np.cos(5.0 * x[i]) * scale2 + 
                           np.sin(7.0 * x[i]) * scale3)
            
        # Exponential decay interaction terms
        decay_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                weight = np.exp(-dist**2 / 4.0)
                decay_interaction += weight * (np.sin(2.0 * x[i]) * np.cos(1.5 * x[j]) + 
                                             np.cos(1.0 * x[i]) * np.sin(2.5 * x[j]))
                
        # Dynamic resonance with phase coupling
        resonance = 0
        for i in range(self.dim):
            phase = np.pi * np.sin(0.5 * x[i])
            resonance += (np.sin(x[i] + phase) * np.cos(x[i] - phase) * 
                         np.exp(-0.2 * (x[i] - 1.0)**2))
            
        # Fractional Brownian motion inspired component
        fbm = 0
        for i in range(self.dim):
            fbm += (np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) * 
                   np.exp(-0.1 * (x[i] - 2.0)**2) * 
                   np.sin(0.1 * i) + 
                   np.cos(6.0 * x[i]) * np.sin(2.0 * x[i]) * 
                   np.exp(-0.15 * (x[i] + 1.5)**2) * 
                   np.cos(0.1 * i))
        
        # Adaptive noise modulation
        noise_mod = 0
        for i in range(self.dim):
            noise_mod += np.sin(x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.05 * x[i]**2) * (1 + 0.1 * np.sin(i))
            
        # Combine components with carefully tuned weights
        return (base * 0.15 + 
                chaotic_osc * 0.35 + 
                multi_scale * 0.25 + 
                decay_interaction * 0.15 + 
                resonance * 0.05 + 
                fbm * 0.03 + 
                noise_mod * 0.02)