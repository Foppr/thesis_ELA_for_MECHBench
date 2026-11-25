import numpy as np

class FractalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base separable quadratic term
        base = 0.1 * np.sum(x**2)
        
        # Fractal-like trigonometric component with self-similarity
        fractal_trig = 0
        for i in range(self.dim):
            # Multi-scale periodic components with varying frequencies and amplitudes
            freqs = [1.0, 2.5, 4.0, 6.2]
            scale_idx = i % len(freqs)
            freq = freqs[scale_idx]
            
            # Self-similar structure using recursive-like modulation
            modulator = np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.exp(-0.1 * x[i]**2)
            fractal_trig += modulator * (1.0 + 0.2 * np.sin(0.3 * i))
        
        # Dynamic conditioning component with dimension-dependent scaling
        conditioning = 0
        for i in range(self.dim):
            # Varying condition numbers based on dimension index
            cond_factor = 1.0 + 2.5 * np.sin(0.2 * i) * np.cos(0.1 * i)
            conditioning += (x[i]**2) * cond_factor
        
        # Multi-modal landscape with clustered peaks and valleys
        multimodal = 0
        for i in range(self.dim):
            # Clustered local optima with varying heights and positions
            peak_positions = [2.0, -2.0, 1.0, -1.0]
            pos_idx = i % len(peak_positions)
            peak_pos = peak_positions[pos_idx]
            
            # Gaussian-like peaks with dynamic widths and heights
            peak_height = 1.0 + 0.5 * np.sin(0.4 * i)
            width = 0.8 + 0.3 * np.cos(0.3 * i)
            
            multimodal += peak_height * np.exp(-0.5 * ((x[i] - peak_pos) / width)**2)
        
        # Cross-dimensional interaction with fractal coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Fractal-like coupling between dimensions
                coupling_strength = 0.5 + 0.3 * np.sin(0.2 * (i + j)) * np.cos(0.1 * i)
                interaction += coupling_strength * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Asymmetric component with chaotic modulation
        asymmetric = 0
        for i in range(self.dim):
            # Asymmetric oscillation with varying phases and amplitudes
            phase_shift = 0.5 * np.sin(0.3 * i)
            asym_term = np.sin(x[i] + phase_shift) * np.cos(x[i] - phase_shift) * np.exp(-0.1 * x[i]**2)
            asymmetric += asym_term * (1.0 + 0.15 * np.sin(0.4 * i))
        
        # Basin structure with varying depths and locations
        basin_structure = 0
        for i in range(self.dim):
            # Chaotic basin boundaries
            basin_loc = 1.5 * np.sin(0.3 * i) * (1.0 + 0.1 * np.cos(i * 0.2))
            basin_depth = 0.8 + 0.2 * np.sin(0.4 * i)
            basin_structure += basin_depth * (np.exp(-0.3 * (x[i] - basin_loc)**2) + 
                                             np.exp(-0.2 * (x[i] + basin_loc)**2))
        
        # Enhanced nonlinearity through polynomial and trigonometric mixing
        nonlinear = 0
        for i in range(self.dim):
            # Mixed polynomial and trigonometric terms with dynamic scaling
            poly_term = x[i]**3 * np.sin(x[i])
            trig_term = np.cos(x[i]**2) * np.exp(-0.1 * (x[i] - 1.0)**2)
            nonlinear += (poly_term + trig_term) * (1.0 + 0.1 * np.sin(0.2 * i))
        
        # Combine all components with optimized weights
        return (base * 0.8 +
                fractal_trig * 0.6 +
                conditioning * 0.4 +
                multimodal * 0.5 +
                interaction * 0.3 +
                asymmetric * 0.25 +
                basin_structure * 0.35 +
                nonlinear * 0.4)