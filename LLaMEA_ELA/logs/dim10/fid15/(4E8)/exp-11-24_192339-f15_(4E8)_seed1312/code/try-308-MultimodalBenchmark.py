import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired phase coupling with dynamic modulation
        quantum_phase = 0
        for i in range(self.dim):
            phase_mod = np.sin(0.3 * x[i]) * np.cos(0.7 * x[i])
            coupling = np.exp(-0.2 * (x[i] - 1.0)**2) * np.sin(2.0 * x[i] + phase_mod)
            quantum_phase += coupling
        
        # Dynamic fractal wavelets with multi-scale oscillations
        fractal_wavelet = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(0.5 * x[i])
            wavelet_component = np.exp(-0.5 * ((x[i] - 2.0) / (0.5 * scale_factor))**2) * \
                               np.sin(scale_factor * x[i]) * np.cos(0.3 * x[i])
            fractal_wavelet += wavelet_component
        
        # Adaptive spectral resonance with frequency locking
        spectral_resonance = 0
        for i in range(self.dim):
            freq_lock = 1.5 + 0.5 * np.cos(0.4 * x[i])
            resonance = np.sin(freq_lock * x[i]) * np.exp(-0.1 * x[i]**2)
            spectral_resonance += resonance
        
        # Energy landscape with dynamic curvature and saddle points
        energy_landscape = 0
        for i in range(self.dim):
            dynamic_curvature = 1.0 + 0.3 * np.sin(0.6 * x[i]) + 0.2 * np.cos(0.8 * x[i])
            energy_landscape += dynamic_curvature * (x[i]**4 - 4*x[i]**2 + 4) + \
                               0.5 * np.sin(1.2 * x[i]) * np.cos(0.9 * x[i])
        
        # Coupled nonlinear interactions with memory effects
        coupled_interaction = 0
        for i in range(self.dim):
            for j in range(max(0, i-3), i):  # Memory-based coupling
                memory_factor = 0.7 + 0.3 * np.sin(0.2 * (x[i] - x[j]))
                interaction = memory_factor * np.cos(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                coupled_interaction += interaction
        
        # Adaptive conditioning and dimensionality scaling
        condition_factor = 1.0 + 0.25 * np.sin(0.3 * self.dim) + 0.15 * np.cos(0.2 * self.dim)
        
        # Combine all components with optimized weights for better algorithm discrimination
        return condition_factor * (0.25 * quantum_phase + 
                                  0.2 * fractal_wavelet + 
                                  0.25 * spectral_resonance + 
                                  0.2 * energy_landscape + 
                                  0.1 * coupled_interaction)