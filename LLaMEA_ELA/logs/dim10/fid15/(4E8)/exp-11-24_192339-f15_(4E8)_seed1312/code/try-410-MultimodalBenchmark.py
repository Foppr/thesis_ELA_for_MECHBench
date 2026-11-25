import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired harmonic oscillators with adaptive frequencies
        quantum = 0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[i]**2)
            amp = 1.0 + 0.5 * np.sin(0.6 * x[i])
            quantum += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Fractal potential wells with adaptive scaling and dynamic transitions
        fractal_potential = 0
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(0.5 * x[i])
            well_depth = 2.0 + 1.0 * np.cos(0.3 * x[i]**2)
            fractal_potential += well_depth * np.exp(-scale * (x[i] - np.sin(x[i]))**2) * np.sin(0.4 * x[i]**3)
        
        # Dynamic saddle-point modulation with chaotic coupling
        saddle = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling_strength = 0.5 + 0.5 * np.sin(0.2 * (x[i] + x[j]))
                saddle += coupling_strength * np.tanh(x[i]) * np.tanh(x[j]) * np.exp(-0.2 * (x[i] - x[j])**2)
        
        # Multi-scale chaotic ridge structures with variable curvature
        ridges = 0
        for i in range(self.dim):
            curvature = 1.0 + 0.8 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i]**2)
            ridge_height = 1.5 + 0.5 * np.sin(0.3 * x[i]**3)
            ridges += ridge_height * np.exp(-curvature * (x[i] - np.sin(0.4 * x[i]))**2) * np.cos(0.6 * x[i])
        
        # Adaptive oscillatory components with time-varying phase modulation
        adaptive_oscillation = 0
        for i in range(self.dim):
            phase_mod = 1.0 + 0.3 * np.sin(0.5 * x[i]**2)
            freq_mod = 1.8 + 0.7 * np.cos(0.4 * x[i])
            adaptive_oscillation += np.sin(freq_mod * x[i] + phase_mod) * np.exp(-0.15 * x[i]**2)
        
        # Enhanced basin structure with quantum tunneling probability
        basin = 0
        for i in range(self.dim):
            tunnel_prob = 0.5 * (1.0 + np.tanh(0.5 * x[i]))
            basin += tunnel_prob * (x[i]**8 - 4*x[i]**6 + 6*x[i]**4 - 4*x[i]**2 + 1)
        
        # Combine all components with optimized weights for maximum complexity
        return 0.25 * quantum + 0.25 * fractal_potential + 0.20 * saddle + 0.15 * ridges + 0.10 * adaptive_oscillation + 0.05 * basin