import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute time-varying parameters for dynamic behavior
        self.t = 0.0
    
    def f(self, x):
        self.t += 0.01  # Increment time for dynamic effects
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with harmonic modulation
        chaotic_grad = 0.0
        for i in range(self.dim):
            freq = 2.5 + 1.2 * np.sin(0.35 * self.t + i)
            amp = 1.2 + 0.4 * np.cos(0.25 * self.t + i)
            chaotic_grad += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Adaptive penalty regions based on solution density
        penalty = 0.0
        for i in range(self.dim):
            if abs(x[i]) > 4.0:
                penalty += 12.0 * (abs(x[i]) - 4.0)**2
            elif abs(x[i]) < 0.3:
                penalty += 6.0 * (0.3 - abs(x[i]))**2
        
        # Multi-scale fractal interference with varying coupling strengths
        fractal_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.6 + 0.25 * np.sin(0.45 * self.t + i + j)
                dist = np.abs(x[i] - x[j])
                fractal_interference += coupling_strength * np.exp(-dist**2) * np.sin(2.5 * dist)
        
        # Time-varying harmonic potentials with dynamic amplitudes and phases
        harmonic_potential = 0.0
        for i in range(self.dim):
            amp = 1.1 + 0.35 * np.sin(0.55 * self.t + i)
            phase = 0.25 * np.cos(0.45 * self.t + i)
            harmonic_potential += amp * (x[i]**2) * np.cos(phase + x[i])
        
        # Polynomial scaling with dimensionality-dependent adjustment
        poly_scale = 1.0 + 0.12 * np.log(self.dim + 1) if self.dim > 0 else 1.0
        
        # Combine all components with dynamic weights
        weight1 = 0.35 + 0.15 * np.sin(0.35 * self.t)
        weight2 = 0.45 + 0.15 * np.cos(0.25 * self.t)
        weight3 = 0.25 + 0.15 * np.sin(0.45 * self.t)
        
        result = weight1 * chaotic_grad + weight2 * fractal_interference + weight3 * harmonic_potential + penalty
        return result * poly_scale