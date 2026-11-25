import numpy as np

class FractalQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with fractal scaling
        r = np.sqrt(np.sum(x**2))
        result = 0.05 * r**2
        
        # Fractal ridge structure with self-similar patterns
        for i in range(self.dim):
            # Create fractal-like ridges using recursive sine components
            ridge_term = 0.0
            for k in range(1, 6):
                freq = 2**k * (1 + 0.1 * np.sin(i * 0.3 + r * 0.05))
                amp = 1.0 / (2**k) * (1 + 0.05 * np.cos(i * 0.2 + r * 0.03))
                ridge_term += amp * np.sin(freq * x[i])
            result += 0.5 * ridge_term**2
            
        # Quantum tunneling effect with probabilistic potential wells
        for i in range(self.dim):
            # Create quantum-like wells with dynamic positions and heights
            well_pos = 3.0 * np.sin(i * 0.4 + r * 0.1)
            well_height = 2.0 + 0.8 * np.cos(i * 0.3 + r * 0.08)
            well_width = 0.8 + 0.2 * np.sin(i * 0.5 + r * 0.12)
            
            # Quantum tunneling potential
            tunnel_potential = well_height * np.exp(-0.5 * ((x[i] - well_pos) / well_width)**2)
            result += tunnel_potential
            
        # Dynamic energy landscape with time-varying harmonic components
        time_factor = 1.0 + 0.3 * np.sin(r * 0.2 + self.dim * 0.1)
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i * 0.4 + r * 0.07)
            result += time_factor * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        # Multi-scale interference patterns with fractal frequency modulation
        for i in range(self.dim):
            scale = 2**(i % 4 + 1) * (1.0 + 0.1 * np.sin(i * 0.2))
            result += 0.8 * np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.25)
            
        # Asymmetric barrier potentials with quantum-like tunneling
        for i in range(self.dim):
            barrier_pos = 4.0 * np.sin(i * 0.3 + r * 0.06)
            barrier_height = 1.5 + 0.7 * np.cos(i * 0.2 + r * 0.09)
            
            # Asymmetric penalty with tunneling effect
            dist = np.abs(x[i] - barrier_pos)
            result += barrier_height * (dist**2 + 0.01) / (dist**2 + 0.01 + 0.05 * np.sin(r * 0.15))
            
        # Cross-dimensional coupling with quantum entanglement effect
        for i in range(self.dim):
            coupling = 0.0
            for j in range(i+1, min(i+3, self.dim)):
                # Quantum entanglement term
                entangle = np.sin(0.5 * (x[i] - x[j])) * np.cos(0.5 * (x[i] + x[j]))
                coupling += 0.4 * entangle * (1 + 0.2 * np.sin(i * j * 0.2 + r * 0.05))
            result += coupling
            
        # Fractal basin boundaries with chaotic positioning
        basin_positions = []
        for i in range(self.dim):
            pos = 3.5 * np.sin(i * 0.5 + r * 0.1)
            basin_positions.append(pos)
            
        for i in range(self.dim):
            dist_to_basin = np.abs(x[i] - basin_positions[i % len(basin_positions)])
            result += 0.6 * np.exp(-dist_to_basin**2) * (1 + 0.15 * np.sin(r * 0.2))
            
        # Additional chaotic harmonic components
        chaos_freq = 3.0 + 1.5 * np.sin(r * 0.15)
        for i in range(self.dim):
            result += 0.4 * np.sin(chaos_freq * x[i] + 0.5 * np.cos(i * 0.3)) * np.cos(chaos_freq * x[i] * 0.2)
            
        # Mutation: Slightly modified coupling strengths and harmonic frequencies
        # Increased coupling strength from 0.4 to 0.5
        for i in range(self.dim):
            coupling = 0.0
            for j in range(i+1, min(i+3, self.dim)):
                entangle = np.sin(0.5 * (x[i] - x[j])) * np.cos(0.5 * (x[i] + x[j]))
                # Modified frequency modulation factor
                coupling += 0.5 * entangle * (1 + 0.25 * np.sin(i * j * 0.25 + r * 0.06))
            result += coupling
            
        # Increased harmonic frequency for dynamic components
        time_factor = 1.0 + 0.3 * np.sin(r * 0.25 + self.dim * 0.1)
        for i in range(self.dim):
            freq = 2.5 + 0.6 * np.sin(i * 0.45 + r * 0.08)
            result += time_factor * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
            
        return result