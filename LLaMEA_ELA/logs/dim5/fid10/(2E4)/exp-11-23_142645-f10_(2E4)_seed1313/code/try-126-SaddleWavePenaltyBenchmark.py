import numpy as np

class SaddleWavePenaltyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine wave components with frequency and amplitude modulation
        wave_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.2 * np.sin(0.5 * x[i]) * np.cos(0.4 * x[i]) + 0.5 * np.sin(1.3 * x[i])
            amp_mod = 1.5 + 0.8 * np.cos(0.6 * x[i]) * np.sin(0.7 * x[i])
            wave_term += amp_mod * freq * np.sin(freq * x[i] + 0.3 * np.cos(2.0 * x[i])) * np.exp(-0.1 * x[i]**2)
        
        # Enhanced adaptive saddle-point conditioning with variable curvature and multi-scale effects
        saddle_condition = 0.0
        for i in range(self.dim):
            curvature = 1.5 + 0.6 * np.sin(0.6 * x[i]) * np.cos(0.8 * x[i])
            curvature += 0.3 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
            saddle_condition += curvature * x[i]**2 * np.exp(-0.15 * np.abs(x[i]))
        
        # Enhanced dynamic penalty regions with multiple zones and overlapping effects
        penalty = 0.0
        for i in range(self.dim):
            # Multiple overlapping penalty zones with varying intensities and shapes
            if np.abs(x[i] - 2.5) < 0.3 or np.abs(x[i] + 2.5) < 0.3:
                penalty += 15.0 * np.exp(-0.5 * (x[i] - 2.5)**2) + 15.0 * np.exp(-0.5 * (x[i] + 2.5)**2)
            elif np.abs(x[i]) < 0.15:
                penalty += 8.0 * np.exp(-0.3 * x[i]**2)
            elif np.abs(x[i] - 1.0) < 0.25 or np.abs(x[i] + 1.0) < 0.25:
                penalty += 10.0 * np.exp(-0.4 * (x[i] - 1.0)**2) + 10.0 * np.exp(-0.4 * (x[i] + 1.0)**2)
            elif np.abs(x[i] - 3.0) < 0.2 or np.abs(x[i] + 3.0) < 0.2:
                penalty += 12.0 * np.exp(-0.35 * (x[i] - 3.0)**2) + 12.0 * np.exp(-0.35 * (x[i] + 3.0)**2)
        
        # Enhanced cross-term coupling with complex phase modulation and interaction kernels
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_mod = np.sin(4.0 * (x[i] + x[j]) + np.cos(3.0 * x[i] - x[j])) + 0.5 * np.sin(2.0 * x[i])
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_coupling += phase_mod * np.exp(-0.2 * dist**2) * (x[i]**2 + x[j]**2 + 0.5 * x[i] * x[j])
        
        # Enhanced asymmetric oscillatory basin with piecewise smooth transitions and fractal-like features
        asym_basin = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                asym_basin += 0.7 * np.sin(2.0 * x[i]) * np.exp(-0.15 * x[i]**2) + 0.3 * x[i]**3 + 0.1 * np.sin(5.0 * x[i])
            else:
                asym_basin += 0.6 * np.cos(1.8 * x[i]) * np.exp(-0.1 * x[i]**2) + 0.2 * x[i]**4 + 0.08 * np.cos(3.0 * x[i])
        
        # Enhanced multi-scale harmonic interference with complex amplitude modulation and noise components
        harmonic = 0.0
        for i in range(self.dim):
            amp_mod = 1.3 + 0.6 * np.cos(0.7 * x[i]) * np.sin(0.9 * x[i]) + 0.2 * np.sin(1.5 * x[i])
            harmonic += amp_mod * np.sin(3.0 * x[i] + 0.7 * np.sin(x[i]) + 0.4 * np.cos(2.0 * x[i])) * np.exp(-0.35 * np.abs(x[i]))
        
        # Additional complexity with novel interaction terms and fractal-like patterns
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended interaction range
                # Fractal-like interaction kernel with multi-scale effects
                scale_factor = 1.0 + 0.3 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[j])
                interaction += scale_factor * (x[i] * x[j]) / (1.0 + np.abs(x[i] - x[j])) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Combined fitness with optimized weights and additional complexity factors
        total = 0.22 * wave_term + 0.27 * saddle_condition + 0.20 * penalty + 0.24 * cross_coupling + 0.10 * asym_basin + 0.06 * harmonic + 0.05 * interaction
        
        return total