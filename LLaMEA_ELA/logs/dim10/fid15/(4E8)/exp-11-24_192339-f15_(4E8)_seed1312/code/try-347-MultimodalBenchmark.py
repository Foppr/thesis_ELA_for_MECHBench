import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired superposition states with entangled phase modulation
        superposition = 0
        for i in range(self.dim):
            # Entangled phase coupling with quantum-like interference
            phase_entanglement = np.sin(2.0 * x[i] + 0.7 * np.sin(1.8 * x[i]) * self.dim)
            # Quantum tunneling probability modulation
            tunneling_prob = 1.0 + 0.5 * np.sin(1.2 * x[i] + 0.3 * np.cos(2.0 * x[i]))
            superposition += tunneling_prob * (x[i]**2) * np.exp(-0.1 * x[i]**2) * phase_entanglement
        
        # Dynamic chaotic attractor landscape with fractal basin structures
        attractor = 0
        for i in range(self.dim):
            # Time-varying chaotic potential with multi-scale oscillations
            chaotic_potential = 1.5 + 0.8 * np.sin(0.9 * x[i] + 0.6 * np.cos(1.3 * x[i]) + self.dim * 0.2)
            attractor += chaotic_potential * np.exp(-0.2 * x[i]**2) * np.sin(1.5 * x[i])**2
        
        # Adaptive ridge structures with dynamic coupling terms
        ridge = 0
        for i in range(self.dim):
            for j in range(max(0, i-3), min(i+3, self.dim)):  # Extended coupling range
                # Dynamic ridge strength based on dimensionality and position
                ridge_strength = 1.0 + 0.6 * np.sin(0.5 * (x[i] - x[j]) + self.dim * 0.3)
                distance = np.exp(-0.2 * (x[i] - x[j])**2)
                ridge += ridge_strength * distance * (x[i]**2 + x[j]**2)
        
        # Multi-scale harmonic components with quantum frequency modulation
        harmonic = 0
        for i in range(self.dim):
            # Quantum-like frequency modulation
            freq1 = 3.0 + 1.5 * np.sin(0.7 * x[i] + self.dim * 0.4)
            freq2 = 2.2 + 1.1 * np.cos(0.8 * x[i] + self.dim * 0.3)
            harmonic += (freq1 * np.sin(freq1 * x[i]) + freq2 * np.cos(freq2 * x[i])) * np.exp(-0.1 * x[i]**2)
        
        # Energy basin complexity with adaptive scaling
        basin_complexity = 0
        for i in range(self.dim):
            # Adaptive basin depth based on position and dimensionality
            basin_depth = 0.8 + 0.4 * np.sin(1.1 * x[i] + self.dim * 0.25)
            basin_complexity += basin_depth * np.exp(-0.3 * x[i]**2) * np.cos(1.3 * x[i])**2
        
        # Combined landscape with optimized multi-scale weights and quantum scaling
        fractal_scaling = 1.5 + 0.4 * np.sin(self.dim * 0.9 + 0.3 * np.cos(x[0] if self.dim > 0 else 0)) + 0.2 * np.sin(4.0 * x[0] if self.dim > 0 else 0)
        
        return (0.35 * superposition + 0.25 * attractor + 
                0.2 * ridge + 0.15 * harmonic + 0.05 * basin_complexity) * fractal_scaling