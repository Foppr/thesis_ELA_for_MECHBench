import numpy as np

class QuantumHarmonicSuperpositionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum superposition harmonic components with phase interference
        f1 = 0.0
        for i in range(self.dim):
            phase = np.pi * np.sin(0.32 * i + 0.25 * np.sum(x**2))
            amplitude = 1.0 + 0.3 * np.cos(0.42 * i)
            f1 += amplitude * np.sin(x[i] + phase)**2 * np.exp(-0.12 * x[i]**2)
            
        # Adaptive radial quantum potentials with tunneling effects
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            tunneling_factor = 1.0 + 0.25 * np.sin(0.52 * i + 0.32 * r)
            f2 += tunneling_factor * np.exp(-0.15 * (x[i]**2 - 2.0)**2)  # Changed from 1.5 to 2.0
            
        # Dynamic harmonic coupling with quantum interference patterns
        f3 = 0.0
        for i in range(self.dim):
            coupling_strength = 1.2 + 0.4 * np.cos(0.35 * i + 0.22 * np.sum(x**2))
            f3 += coupling_strength * np.sin(1.5 * x[i])**2 * np.cos(0.7 * x[i])
            
        # Multi-scale quantum harmonic oscillators with adaptive frequencies
        f4 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.42 * i + 0.35 * np.sum(x**2))
            f4 += np.sin(freq * x[i])**4
            
        # Quantum tunneling basin interactions with probabilistic weighting
        f5 = 0.0
        for i in range(self.dim):
            prob_weight = 0.7 + 0.3 * np.cos(0.62 * i)
            f5 += prob_weight * np.exp(-0.18 * x[i]**2) * np.sin(2.0 * x[i])**2
            
        # Adaptive harmonic conditioning with quantum-like phase shifts
        f6 = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.42 * i + 0.25 * np.sum(x**2))
            f6 += (x[i]**2) * np.cos(x[i] + phase_shift)**2
            
        # Radial quantum harmonic resonance with dynamic amplitude modulation
        r = np.sqrt(np.sum(x**2))
        f7 = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.35 * np.cos(0.32 * i + 0.22 * r)
            f7 += amp_mod * np.sin(1.2 * x[i])**3
            
        # Boundary quantum confinement with superposition states
        f8 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                confinement_factor = 1.5 + 0.5 * np.sin(0.62 * i)
                f8 += confinement_factor * np.exp(-0.3 * (5.0 - np.abs(x[i]))**2)
                
        # Cross-dimensional quantum coupling with entanglement effects
        f9 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    entangle_factor = 1.0 + 0.3 * np.cos(0.52 * (i + j) + 0.22 * np.sum(x**2))
                    coupling = x[i] * x[j] * entangle_factor
                    coupling_sum += coupling
            f9 += coupling_sum * np.sin(0.5 * x[i])**2
            
        # Quantum harmonic interference with multi-modal energy landscape
        f10 = 0.0
        for i in range(self.dim):
            interference_term = np.sin(x[i])**2 + np.cos(x[i])**2
            f10 += interference_term * np.exp(-0.15 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10