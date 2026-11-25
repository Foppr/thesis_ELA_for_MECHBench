import numpy as np

class ChaoticEllipticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic cosine wave components with dynamic frequency modulation
        cos_wave = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.6 * np.cos(0.8 * x[i]) * np.sin(0.5 * x[i])
            amp_mod = 1.0 + 0.4 * np.cos(0.7 * x[i]) * np.sin(0.6 * x[i])
            cos_wave += amp_mod * np.cos(freq_mod * x[i] + 0.2 * np.cos(1.3 * x[i])) * np.exp(-0.15 * x[i]**2)
        
        # Adaptive elliptic conditioning with chaotic eccentricity
        elliptic = 0.0
        for i in range(self.dim):
            eccentricity = 1.0 + 0.5 * np.cos(0.6 * x[i]) * np.sin(0.4 * x[i])
            elliptic += eccentricity * (x[i]**2 + 0.4 * np.cos(0.9 * x[i])**2)
        
        # Dynamic gradient modulation with chaotic directionality
        gradient = 0.0
        for i in range(self.dim):
            dir_mod = 1.0 + 0.3 * np.cos(0.5 * x[i]) * np.sin(0.7 * x[i])
            grad_term = dir_mod * (x[i]**3 + 0.3 * np.sin(1.4 * x[i])**2)
            gradient += grad_term
        
        # Enhanced cross-dimensional coupling with chaotic correlation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr = np.cos(1.2 * (x[i] - x[j]) + 0.3 * np.sin(x[i] + x[j]))
                dist = np.sqrt((x[i] - x[j])**2 + 0.15)
                coupling += corr * np.exp(-0.3 * dist**2) * (x[i]**2 + x[j]**2 + 0.2 * x[i] * x[j])
        
        # Multi-scale basin with piecewise chaotic curvature
        basin = 0.0
        for i in range(self.dim):
            if x[i] < -1.5:
                basin += 0.8 * np.cos(1.7 * x[i]) * np.exp(-0.2 * x[i]**2) + 0.25 * x[i]**4
            elif x[i] > 1.5:
                basin += 0.6 * np.sin(1.9 * x[i]) * np.exp(-0.18 * x[i]**2) + 0.15 * x[i]**3
            else:
                basin += 0.3 * x[i]**2 * np.exp(-0.3 * x[i]**2)
        
        # Chaotic harmonic interference with adaptive phase and amplitude
        harmonic = 0.0
        for i in range(self.dim):
            phase = 1.0 + 0.25 * np.cos(0.8 * x[i]) * np.sin(0.6 * x[i])
            amp = 1.0 + 0.35 * np.cos(0.7 * x[i]) * np.sin(0.5 * x[i])
            harmonic += amp * np.cos(phase * x[i] + 0.3 * np.cos(x[i])) * np.exp(-0.25 * np.abs(x[i]))
        
        # Combined fitness with variable weighting and chaotic scaling
        total = 0.2 * cos_wave + 0.25 * elliptic + 0.15 * gradient + 0.2 * coupling + 0.15 * basin + 0.05 * harmonic
        
        return total