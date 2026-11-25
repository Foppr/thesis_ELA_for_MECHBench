import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay interactions with chaotic coupling
        exp_decay = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                dist = np.abs(x[i] - x[j])
                exp_decay += np.exp(-dist) * np.sin(5 * dist) * np.cos(2 * x[i] * x[j])
        
        # Polynomial saddle points with varying curvature
        saddle_points = 0.0
        for i in range(self.dim):
            saddle_points += (x[i]**4 - 6*x[i]**2 + 9) * np.exp(-0.1 * x[i]**2)
        
        # Quantum-like probability distribution peaks
        quantum_peaks = 0.0
        for i in range(self.dim):
            peak_pos = 3.0 * np.sin(i * np.pi / self.dim)
            width = 0.8 + 0.4 * np.cos(i * np.pi / self.dim)
            height = 1.5 + 0.5 * np.sin(i * np.pi / (self.dim + 1))
            quantum_peaks += height * np.exp(-0.5 * ((x[i] - peak_pos) ** 2) / (width ** 2)) * np.cos(4 * x[i])
        
        # Cross-dimensional trigonometric coupling with phase shifts
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_shift = np.sin(i * j * 0.5)
                cross_coupling += np.sin(x[i] + x[j] + phase_shift) * np.cos(2 * (x[i] - x[j]))
        
        # Adaptive penalty corridors with dynamic boundaries
        penalties = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                penalties += (np.abs(x[i]) - 4.0)**3 * np.exp(-0.5 * (x[i] ** 2))
            elif np.abs(x[i]) > 3.0:
                penalties += (np.abs(x[i]) - 3.0)**2 * np.sin(x[i])
        
        # Multi-scale harmonic oscillations with frequency modulation
        harmonic_osc = 0.0
        for i in range(self.dim):
            freq = 1 + 0.5 * np.sin(i)
            harmonic_osc += np.sin(freq * x[i]) * np.cos(2 * freq * x[i]) * np.exp(-0.03 * i)
        
        # Mixed hyperbolic and exponential interactions
        mixed_hyp_exp = 0.0
        for i in range(self.dim):
            mixed_hyp_exp += (np.tanh(x[i]) * np.exp(-x[i]**2)) + (1 / (1 + np.exp(-x[i])) - 0.5)
        
        # Combined fitness with carefully balanced weights
        return 0.3 * exp_decay + 0.25 * saddle_points + 0.2 * quantum_peaks + 0.1 * cross_coupling + 0.1 * penalties + 0.05 * harmonic_osc + 0.05 * mixed_hyp_exp