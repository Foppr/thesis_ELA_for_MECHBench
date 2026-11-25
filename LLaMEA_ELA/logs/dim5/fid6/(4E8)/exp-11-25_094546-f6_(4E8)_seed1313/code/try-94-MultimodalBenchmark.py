import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum superposition component with probabilistic weighting
        quantum = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Superposition of multiple wave functions with random phases
            phase1 = np.sin(xi * 10.0) * np.cos(xi * 7.0)
            phase2 = np.cos(xi * 13.0) * np.sin(xi * 5.0)
            phase3 = np.sin(xi * 8.0) * np.sin(xi * 9.0)
            quantum += (phase1 + phase2 + phase3) / 3.0
        
        # Entangled dimension coupling with modified quantum correlation
        entanglement = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified entanglement strength with different decay
                dist = np.abs(x_norm[i] - x_norm[j])
                corr_strength = np.exp(-dist**2 * 3.0) * np.sin(dist * np.pi * 1.5)
                entanglement += corr_strength * (x_norm[i]**2 + x_norm[j]**2)
        
        # Dynamic phase interference with altered frequencies
        phase_interference = 0.0
        for i in range(self.dim):
            # Phase evolution based on position and dimension index
            phase = (x_norm[i] * (i + 1) * 0.5) % (2 * np.pi)
            # Modified interference pattern with different frequencies
            interference = np.sin(phase * 4.0) * np.cos(phase * 3.0) * np.sin(phase * 6.0)
            phase_interference += interference
        
        # Probabilistic basin boundaries with quantum tunneling effects
        basins = 0.0
        for i in range(self.dim):
            # Create quantum-like tunneling regions with different scaling
            tunnel = np.exp(-np.abs(x_norm[i]) * 4.0) * np.sin(x_norm[i] * 12.0)
            basins += tunnel
        
        # Adaptive amplitude modulation based on dimensionality
        amp_modulation = 1.0 + 0.3 * np.sin(self.dim * 0.4) * np.cos(self.dim * 0.2)
        
        # Modified energy landscape with altered curvature
        energy = 0.0
        for i in range(self.dim):
            energy += (x_norm[i]**5 - 2.5 * x_norm[i]**3 + 1.5 * x_norm[i]**2) * np.exp(-0.3 * x_norm[i]**2)
        
        # Combine all quantum components with dynamic weights
        weight_quantum = 0.3 + 0.1 * np.sin(self.dim * 0.3)
        weight_entanglement = 0.4 + 0.15 * np.cos(self.dim * 0.2)
        weight_phase = 0.2 + 0.05 * np.sin(self.dim * 0.1)
        weight_basins = 0.1 + 0.05 * np.cos(self.dim * 0.4)
        weight_energy = 0.25 + 0.05 * np.sin(self.dim * 0.3)
        
        return amp_modulation * (weight_quantum * quantum + 
                                weight_entanglement * entanglement + 
                                weight_phase * phase_interference + 
                                weight_basins * basins + 
                                weight_energy * energy)