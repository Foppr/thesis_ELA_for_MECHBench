import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.02  # Faster time increment for increased dynamics
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient with stochastic modulation
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = 1.5 + 2.0 * np.sin(0.4 * self.t + i * 0.7)
            amp = 0.8 + 1.2 * np.cos(0.3 * self.t + i * 0.5)
            chaotic_grad += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + self.t * 0.1)
        
        # Enhanced penalty with multi-modal structure
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.2:
                penalty += 15.0 * (abs(x[i]) - 4.2)**2.5
            elif abs(x[i]) < 0.3:
                penalty += 8.0 * (0.3 - abs(x[i]))**3
        
        # Multi-scale fractal interference with stochastic coupling
        fractal_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.6 + 0.4 * np.sin(0.5 * self.t + i * 0.3 + j * 0.2)
                dist = np.abs(x[i] - x[j])
                fractal_interference += coupling_strength * np.exp(-dist**1.8) * np.sin(3.0 * dist + self.t * 0.05)
        
        # Stochastic harmonic potentials with phase shifts
        harmonic_potential = 0.0
        for i in range(self.dim):
            amp = 1.2 + 0.8 * np.sin(0.6 * self.t + i * 0.4)
            phase = 0.3 * np.cos(0.5 * self.t + i * 0.3) + 0.1 * np.sin(self.t * 0.2)
            harmonic_potential += amp * (x[i]**3) * np.cos(phase + x[i]**2)
        
        # Dimensionality-adaptive scaling with chaotic modulation
        poly_scale = 1.5 + 0.2 * np.sin(0.4 * self.t) + 0.1 * np.log(self.dim + 1)
        
        # Dynamic weighting with stochastic components
        weight1 = 0.25 + 0.15 * np.sin(0.35 * self.t + 0.5)
        weight2 = 0.45 + 0.1 * np.cos(0.25 * self.t + 0.3)
        weight3 = 0.3 + 0.1 * np.sin(0.4 * self.t + 0.7)
        
        result = weight1 * chaotic_grad + weight2 * fractal_interference + weight3 * harmonic_potential + penalty
        return result * poly_scale