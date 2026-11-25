import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute time-varying parameters for dynamic behavior
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.01  # Increment time for dynamic effects
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with enhanced non-linearity
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = 3.0 + 1.5 * np.sin(0.4 * self.t + i * 0.7)
            amp = 1.5 + 0.5 * np.cos(0.3 * self.t + i * 0.5)
            chaotic_grad += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.tanh(x[i])
        
        # Enhanced adaptive penalty regions with exponential scaling
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.2:
                penalty += 15.0 * np.exp(2.0 * (abs(x[i]) - 4.2))
            elif abs(x[i]) < 0.25:
                penalty += 8.0 * (0.25 - abs(x[i]))**3
        
        # Multi-scale fractal interference with dynamic coupling and phase modulation
        fractal_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Limited coupling for scalability
                coupling_strength = 0.7 + 0.3 * np.sin(0.5 * self.t + i * 0.4 + j * 0.3)
                phase_shift = 0.2 * np.cos(0.3 * self.t + i * 0.2 + j * 0.1)
                dist = np.abs(x[i] - x[j])
                fractal_interference += coupling_strength * np.exp(-dist**2) * np.sin(3.0 * dist + phase_shift)
        
        # Time-varying harmonic potentials with stochastic amplitude modulation
        harmonic_potential = 0.0
        for i in range(self.dim):
            amp = 1.3 + 0.4 * np.sin(0.6 * self.t + i * 0.5) * np.cos(0.4 * self.t + i * 0.3)
            phase = 0.3 * np.sin(0.5 * self.t + i * 0.2) + 0.1 * np.cos(0.3 * self.t + i * 0.1)
            harmonic_potential += amp * (x[i]**3) * np.cos(phase + x[i]**2)
        
        # Polynomial scaling with enhanced dimensionality dependence
        poly_scale = 1.0 + 0.15 * np.log(self.dim + 1) + 0.02 * self.dim**0.7 if self.dim > 0 else 1.0
        
        # Dynamic weights with higher frequency modulation for increased complexity
        weight1 = 0.4 + 0.2 * np.sin(0.5 * self.t)
        weight2 = 0.35 + 0.18 * np.cos(0.4 * self.t)
        weight3 = 0.25 + 0.17 * np.sin(0.6 * self.t)
        
        result = weight1 * chaotic_grad + weight2 * fractal_interference + weight3 * harmonic_potential + penalty
        return result * poly_scale