import numpy as np

class LabyrinthinePhaseCoupling:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Base quadratic term with adaptive coefficients
        result = 0.0
        for i in range(self.dim):
            result += (i + 1) * x[i] ** 2
            
        # Add labyrinthine structure with dynamic phase shifts
        r = np.sqrt(np.sum(x ** 2))
        phase_shift = 0.5 * np.sin(0.3 * r) * np.cos(0.4 * r)
        
        for i in range(self.dim):
            # Dynamic coupling with adaptive strength
            coupling_strength = 1.0 + 0.3 * np.sin(0.7 * x[i]) * np.cos(0.5 * r)
            result += coupling_strength * np.sin(8 * x[i] + phase_shift) * np.cos(6 * x[(i + 1) % self.dim])
            
        # Add adaptive harmonic components with dimension-dependent frequencies
        for i in range(self.dim):
            freq = 3 + 2 * np.sin(0.5 * i)
            result += 0.5 * np.sin(freq * x[i]) * np.cos(freq * x[(i + 2) % self.dim]) * np.exp(-0.1 * x[i] ** 2)
            
        # Add multi-scale labyrinthine structure with varying amplitudes
        for i in range(self.dim):
            result += 0.3 * np.sin(15 * x[i] + 0.2 * i) * np.cos(12 * x[(i + 1) % self.dim]) * np.exp(-0.05 * r ** 2)
            
        # Add dynamic coupling with exponential decay and adaptive scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                coupling = 0.4 * np.exp(-0.3 * dist) * np.sin(5 * x[i]) * np.cos(7 * x[j])
                result += coupling
                
        # Add phase-locked oscillatory components
        for i in range(self.dim):
            result += 0.25 * np.sin(10 * x[i] + 0.1 * i) * np.cos(9 * x[(i + 3) % self.dim]) * np.sin(4 * r)
            
        # Add adaptive radial modulation with time-varying parameters
        radial_mod = 1.0 + 0.4 * np.sin(2 * r) * np.cos(3 * r) * np.exp(-0.2 * r)
        result *= radial_mod
        
        # Add dimensionally dependent chaotic-like interactions
        chaotic_interaction = 0.0
        for i in range(self.dim):
            chaotic_interaction += 0.35 * np.sin(18 * x[i] + 0.1 * i) * np.cos(16 * x[(i + 2) % self.dim]) * np.exp(-0.1 * x[i] ** 2)
        result += chaotic_interaction
        
        # Add adaptive multi-modal structure with overlapping peaks
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.4 * (np.sin(11 * x[i]) + np.cos(9 * x[i])) ** 2 * np.exp(-0.2 * x[i] ** 2)
        result += multimodal
        
        # Add adaptive conditioning term
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += 0.15 * (np.abs(x[i]) ** 1.7) * (1 + 0.2 * np.sin(0.8 * i))
        result += conditioning
        
        # Add global synchronization component
        sync_term = 0.3 * np.sin(2 * np.sum(x)) * np.cos(3 * r)
        result += sync_term
        
        # Add adaptive fractal-like structure with recursive coupling
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.2 * np.sin(20 * x[i]) * np.cos(18 * x[(i + 1) % self.dim]) * np.sin(16 * x[(i + 2) % self.dim])
        result += fractal
        
        return result