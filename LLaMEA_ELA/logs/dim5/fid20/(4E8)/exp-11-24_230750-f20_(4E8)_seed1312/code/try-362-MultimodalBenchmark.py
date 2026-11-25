import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with adaptive exponents
        poly_chaos = 0.0
        for i in range(self.dim):
            exp_factor = 2.0 + 1.5 * np.sin(0.3 * x[i])
            poly_chaos += (x[i]**exp_factor) * np.cos(0.5 * x[i]) * np.sin(0.7 * x[i])
        
        # Trigonometric interference with dynamic frequencies and amplitudes
        trig_interference = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.8 * np.cos(0.4 * x[i])
            amp = 1.5 + 1.2 * np.sin(0.6 * x[i])
            trig_interference += amp * np.sin(freq * x[i] + 0.3 * np.cos(2.0 * x[i]))
        
        # Adaptive conditioning with dimensionally varying parameters
        cond_factor = 0.0
        for i in range(self.dim):
            cond_param = 1.0 + 0.5 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i])
            cond_factor += cond_param * x[i]**2
        
        # Cross-dimensional coupling with harmonic interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling_strength = 0.5 + 0.3 * np.sin(0.4 * (x[i] + x[j]))
                cross_coupling += coupling_strength * np.sin(0.8 * x[i]) * np.cos(0.6 * x[j])
        
        # Asymmetric Gaussian peaks with dynamic widths and heights
        gaussian_peaks = 0.0
        for i in range(self.dim):
            for j in range(3):
                peak_height = 2.0 + 1.0 * np.sin(0.5 * x[i] + j)
                peak_width = 0.5 + 0.3 * np.cos(0.4 * x[i])
                gaussian_peaks += peak_height * np.exp(-0.5 * ((x[i] - j) / peak_width)**2)
        
        # Saddle-point structure with chaotic modulation
        saddle_structure = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                modulator = 0.8 + 0.4 * np.sin(0.6 * x[i]) * np.cos(0.5 * x[i+1])
                saddle_structure += (x[i]**2 - x[i+1]**2) * modulator
        
        # Dimensionally varying harmonic potential
        harmonic_potential = 0.0
        for i in range(self.dim):
            harmonic_freq = 1.0 + 0.5 * np.sin(0.3 * x[i])
            harmonic_potential += np.sin(harmonic_freq * x[i]) * np.cos(0.7 * x[i])
        
        # Final normalization and combination
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        return (0.25 * poly_chaos + 0.20 * trig_interference + 0.15 * cond_factor + 
                0.12 * cross_coupling + 0.10 * gaussian_peaks + 0.08 * saddle_structure + 
                0.07 * harmonic_potential) * dim_factor