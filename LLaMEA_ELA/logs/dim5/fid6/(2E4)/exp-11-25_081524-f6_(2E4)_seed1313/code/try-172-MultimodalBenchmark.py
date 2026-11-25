import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient with modified modulation
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.5 * self.t + i * 0.8)
            amp = 1.0 + 0.9 * np.cos(0.4 * self.t + i * 0.6)
            chaotic_grad += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] + self.t * 0.12)
        
        # Modified penalty with sharper transitions
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.3:
                penalty += 20.0 * (abs(x[i]) - 4.3)**2.8
            elif abs(x[i]) < 0.25:
                penalty += 10.0 * (0.25 - abs(x[i]))**3.2
        
        # Fractal interference with altered coupling
        fractal_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.7 + 0.3 * np.sin(0.6 * self.t + i * 0.4 + j * 0.25)
                dist = np.abs(x[i] - x[j])
                fractal_interference += coupling_strength * np.exp(-dist**2.0) * np.sin(4.0 * dist + self.t * 0.06)
        
        # Modified harmonic potentials with phase shifts
        harmonic_potential = 0.0
        for i in range(self.dim):
            amp = 1.5 + 0.7 * np.sin(0.7 * self.t + i * 0.5)
            phase = 0.4 * np.cos(0.6 * self.t + i * 0.4) + 0.15 * np.sin(self.t * 0.25)
            harmonic_potential += amp * (x[i]**3) * np.cos(phase + x[i]**2.2)
        
        # Dimensionality-adaptive scaling
        poly_scale = 1.6 + 0.15 * np.sin(0.5 * self.t) + 0.12 * np.log(self.dim + 1)
        
        # Dynamic weighting with new stochastic components
        weight1 = 0.3 + 0.1 * np.sin(0.4 * self.t + 0.6)
        weight2 = 0.5 + 0.08 * np.cos(0.3 * self.t + 0.4)
        weight3 = 0.2 + 0.12 * np.sin(0.35 * self.t + 0.8)
        
        result = weight1 * chaotic_grad + weight2 * fractal_interference + weight3 * harmonic_potential + penalty
        return result * poly_scale